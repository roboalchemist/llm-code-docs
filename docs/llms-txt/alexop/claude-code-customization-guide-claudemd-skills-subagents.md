# Source: https://alexop.dev/posts/claude-code-customization-guide-claudemd-skills-subagents

<!DOCTYPE html><html lang="en" class="scroll-smooth astro-sckkx6r4"> <head><meta charset="UTF-8"><meta name="viewport" content="width=device-width"><link rel="icon" type="image/svg+xml" href="/favicon.svg"><link rel="canonical" href="https://alexop.dev/posts/claude-code-customization-guide-claudemd-skills-subagents/"><meta name="generator" content="Astro v5.16.8"><!-- General Meta Tags --><title>Claude Code Customization: CLAUDE.md, Slash Commands, Skills, and Subagents | alexop.dev</title><meta name="title" content="Claude Code Customization: CLAUDE.md, Slash Commands, Skills, and Subagents | alexop.dev"><meta name="description" content="The complete guide to customizing Claude Code. Compare CLAUDE.md, slash commands, skills, and subagents with practical examples showing when to use each."><meta name="author" content="Alexander Opalic"><link rel="sitemap" href="/sitemap-index.xml"><!-- KaTeX CSS for math rendering --><link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css" integrity="sha384-n8MVd4RsNIU0tAv4ct0nTaAbDJwPJzDEaqSD1odI+WdtXRGWt2kTvGFasHpSy3SV" crossorigin="anonymous"><!-- KaTeX Auto-render Extension --><script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" integrity="sha384-+VBxd3r6XgURycqtZ117nYw44OOcIax56Z4dCRWbxyPt0Koah1uHoK0o4+/RRE05" crossorigin="anonymous"></script><script>
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
    </script><!-- Open Graph / Facebook --><meta property="og:title" content="Claude Code Customization: CLAUDE.md, Slash Commands, Skills, and Subagents | alexop.dev"><meta property="og:description" content="The complete guide to customizing Claude Code. Compare CLAUDE.md, slash commands, skills, and subagents with practical examples showing when to use each."><meta property="og:url" content="https://alexop.dev/posts/claude-code-customization-guide-claudemd-skills-subagents/"><meta property="og:image" content="https://alexop.dev/posts/claude-code-customization-claude-md-slash-commands-skills-and-subagents/index.png"><meta property="og:type" content="article"><!-- Article Published/Modified time --><meta property="article:published_time" content="2025-12-21T00:00:00.000Z"><!-- Twitter --><meta property="twitter:card" content="summary_large_image"><meta property="twitter:url" content="https://alexop.dev/posts/claude-code-customization-guide-claudemd-skills-subagents/"><meta property="twitter:title" content="Claude Code Customization: CLAUDE.md, Slash Commands, Skills, and Subagents | alexop.dev"><meta property="twitter:description" content="The complete guide to customizing Claude Code. Compare CLAUDE.md, slash commands, skills, and subagents with practical examples showing when to use each."><meta property="twitter:image" content="https://alexop.dev/posts/claude-code-customization-claude-md-slash-commands-skills-and-subagents/index.png"><meta name="google-site-verification" content="QV58fXjaYnMlTiRdFU7vB1JiPoClRYialURT2HtWaI4"><!-- Google JSON-LD Structured data --><script type="application/ld+json">{"@context":"https://schema.org","@type":"BlogPosting","headline":"Claude Code Customization: CLAUDE.md, Slash Commands, Skills, and Subagents | alexop.dev","description":"The complete guide to customizing Claude Code. Compare CLAUDE.md, slash commands, skills, and subagents with practical examples showing when to use each.","image":"https://alexop.dev/posts/claude-code-customization-claude-md-slash-commands-skills-and-subagents/index.png","datePublished":"2025-12-21T00:00:00.000Z","author":{"@type":"Person","name":"Alexander Opalic"}}</script><!-- Plausible --><script defer data-domain="alexop.dev" src="/js/script.js"></script><!-- Google Font --><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,200;0,400;0,500;0,600;0,700;1,400;1,600&display=swap" rel="stylesheet"><meta name="theme-color" content="#1d1f21"><meta name="astro-view-transitions-enabled" content="true"><meta name="astro-view-transitions-fallback" content="animate"><script type="module" src="/_astro/ClientRouter.astro_astro_type_script_index_0_lang.CDGfc0hd.js"></script><script src="/toggle-theme.js"></script><link rel="stylesheet" href="/_astro/about.C7UzwVpf.css">
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
</style><style>[data-astro-transition-scope="astro-plk3gbjq-1"] { view-transition-name: claude-code-customization-claude-md-slash-commands-skills-and-subagents; }@layer astro { ::view-transition-old(claude-code-customization-claude-md-slash-commands-skills-and-subagents) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(claude-code-customization-claude-md-slash-commands-skills-and-subagents) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(claude-code-customization-claude-md-slash-commands-skills-and-subagents) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(claude-code-customization-claude-md-slash-commands-skills-and-subagents) { 
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
</style><style>.collapsible:where(.astro-kncz7yy6){display:block!important;width:100%!important;max-width:100%!important;margin:1.5rem 0;border:1px solid rgb(var(--color-border));border-radius:.5rem;overflow:hidden}.collapsible-summary:where(.astro-kncz7yy6){display:flex;align-items:center;gap:.5rem;padding:.75rem 1rem;font-weight:500;cursor:pointer;background:rgb(var(--color-card));-webkit-user-select:none;-moz-user-select:none;user-select:none;list-style:none}.collapsible-summary:where(.astro-kncz7yy6)::-webkit-details-marker{display:none}.collapsible-summary:where(.astro-kncz7yy6):hover{background:rgb(var(--color-card-muted))}.collapsible-icon:where(.astro-kncz7yy6){display:flex;align-items:center;transition:transform .2s ease}.collapsible:where(.astro-kncz7yy6)[open] .collapsible-icon:where(.astro-kncz7yy6){transform:rotate(90deg)}.collapsible-content:where(.astro-kncz7yy6){width:100%!important;max-width:100%!important}.collapsible-content:where(.astro-kncz7yy6) pre{margin:0!important;border-radius:0!important;width:100%!important;max-width:100%!important}.collapsible-content:where(.astro-kncz7yy6)>*:first-child{margin-top:0}.collapsible-content:where(.astro-kncz7yy6)>*:last-child{margin-bottom:0}
</style><style>.prose details.collapsible{display:block!important;width:100%!important;max-width:100%!important}
</style><style>.file-tree__item:where(.astro-o25vlg2d){margin:0;padding:0;position:relative}.file-tree__item:where(.astro-o25vlg2d):before{content:"";position:absolute;left:calc(.5rem + (var(--level) * 1.25rem));top:0;bottom:0;width:1px;background:rgba(var(--color-text-base),.15)}.file-tree__item:where(.astro-o25vlg2d):last-child:before{bottom:50%}.file-tree__item:where(.astro-o25vlg2d):after{content:"";position:absolute;left:calc(.5rem + (var(--level) * 1.25rem));top:50%;width:.75rem;height:1px;background:rgba(var(--color-text-base),.15)}.file-tree__folder:where(.astro-o25vlg2d){margin:0;padding:0}.file-tree__folder:where(.astro-o25vlg2d)>summary:where(.astro-o25vlg2d){list-style:none;cursor:pointer;display:flex;gap:.5rem;align-items:center;padding:.2rem .5rem .2rem calc(1.5rem + (var(--level) * 1.25rem));border-radius:.25rem;transition:background-color .15s ease;line-height:1.6;position:relative}.file-tree__folder:where(.astro-o25vlg2d)>summary:where(.astro-o25vlg2d):hover{background:rgba(var(--color-text-base),.05)}.file-tree__folder:where(.astro-o25vlg2d)[open]>summary:where(.astro-o25vlg2d) .file-tree__caret:where(.astro-o25vlg2d){transform:rotate(90deg)}.file-tree__folder:where(.astro-o25vlg2d):not([open])>summary:where(.astro-o25vlg2d) .file-tree__caret:where(.astro-o25vlg2d){transform:rotate(0)}.file-tree__folder:where(.astro-o25vlg2d)>summary:where(.astro-o25vlg2d)::-webkit-details-marker{display:none}.file-tree__list:where(.astro-o25vlg2d){list-style:none;margin:0;padding:0}.file-tree__file:where(.astro-o25vlg2d){display:flex;gap:.5rem;align-items:center;padding:.2rem .5rem .2rem calc(1.5rem + (var(--level) * 1.25rem));border-radius:.25rem;text-decoration:none;color:inherit;transition:background-color .15s ease;line-height:1.6;position:relative}.file-tree__file:where(.astro-o25vlg2d):hover{background:rgba(var(--color-text-base),.05)}a:where(.astro-o25vlg2d).file-tree__file:hover .file-tree__name:where(.astro-o25vlg2d){color:rgb(var(--color-accent))}.file-tree__icon:where(.astro-o25vlg2d){width:1rem;height:1rem;flex-shrink:0;color:rgba(var(--color-text-base),.4);display:inline-flex;align-items:center;justify-content:center}.file-tree__icon--file:where(.astro-o25vlg2d){color:rgba(var(--color-text-base),.4)}.file-tree__icon--colored:where(.astro-o25vlg2d){color:inherit}.file-tree__icon--text:where(.astro-o25vlg2d){font-weight:600;font-size:.875rem;display:inline-flex;align-items:center;justify-content:center;width:1rem;height:1rem}.file-tree__name:where(.astro-o25vlg2d){white-space:nowrap;transition:color .15s ease;font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,Liberation Mono,Courier New,monospace}.file-tree__comment:where(.astro-o25vlg2d){color:rgba(var(--color-text-base),.5);font-style:italic;margin-left:.5rem;white-space:nowrap;font-size:.9em}.file-tree__caret:where(.astro-o25vlg2d){width:.75rem;height:.75rem;transition:transform .2s ease;flex-shrink:0;color:rgba(var(--color-text-base),.5);font-size:.625rem;display:inline-flex;align-items:center;justify-content:center;transform-origin:center}
</style><style>.file-tree:where(.astro-htwbjus4){font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,Liberation Mono,Courier New,monospace;font-size:.8125rem;background:rgb(var(--color-card));color:rgb(var(--color-text-base));border:1px solid rgba(var(--color-border),.5);border-radius:.5rem;padding:.75rem;margin:1.5rem 0;overflow-x:auto}.file-tree__list:where(.astro-htwbjus4){list-style:none;margin:0;padding:0}.file-tree__list:where(.astro-htwbjus4)>li:where(.astro-htwbjus4):first-child:before,.file-tree__list:where(.astro-htwbjus4)>li:where(.astro-htwbjus4):first-child:after{display:none}.file-tree:where(.astro-htwbjus4)::-webkit-scrollbar{height:.5rem}.file-tree:where(.astro-htwbjus4)::-webkit-scrollbar-track{background:rgb(var(--color-fill))}.file-tree:where(.astro-htwbjus4)::-webkit-scrollbar-thumb{background:rgb(var(--color-border));border-radius:.25rem}.file-tree:where(.astro-htwbjus4)::-webkit-scrollbar-thumb:hover{background:rgb(var(--color-card-muted))}
</style><style>.internal-link-wrapper:where(.astro-3tyn5ojg){position:relative;display:inline-block}.internal-link:where(.astro-3tyn5ojg){--tw-text-opacity: 1;color:rgba(var(--color-accent),var(--tw-text-opacity, 1));text-decoration-line:underline;text-decoration-style:dashed;text-decoration-thickness:1px;text-underline-offset:4px;transition-property:all;transition-timing-function:cubic-bezier(.4,0,.2,1);transition-duration:.15s}.internal-link:where(.astro-3tyn5ojg):hover{text-decoration-style:solid}.internal-link:where(.astro-3tyn5ojg){cursor:pointer;display:inline}.preview-card:where(.astro-3tyn5ojg){display:block;position:absolute;bottom:calc(100% + 8px);left:50%;transform:translate(-50%);z-index:9999;width:320px;max-width:90vw;border-radius:.5rem;border-width:1px;--tw-border-opacity: 1;border-color:rgba(var(--color-border),var(--tw-border-opacity, 1));--tw-bg-opacity: 1;background-color:rgba(var(--color-card),var(--tw-bg-opacity, 1));--tw-shadow: 0 10px 15px -3px rgb(0 0 0 / .1), 0 4px 6px -4px rgb(0 0 0 / .1);--tw-shadow-colored: 0 10px 15px -3px var(--tw-shadow-color), 0 4px 6px -4px var(--tw-shadow-color);box-shadow:var(--tw-ring-offset-shadow, 0 0 #0000),var(--tw-ring-shadow, 0 0 #0000),var(--tw-shadow);opacity:0;visibility:hidden;transition:opacity .2s ease-in-out,visibility .2s ease-in-out}.preview-card:where(.astro-3tyn5ojg).is-fixed{position:fixed!important;bottom:auto!important;top:var(--pc-top, 0px)!important;left:var(--pc-left, 0px)!important;transform:none!important}.preview-content:where(.astro-3tyn5ojg){display:block;padding:1rem}.preview-title:where(.astro-3tyn5ojg){display:block;margin-bottom:.5rem;font-size:1rem;line-height:1.5rem;font-weight:600;--tw-text-opacity: 1;color:rgba(var(--color-text-base),var(--tw-text-opacity, 1));line-height:1.3}.preview-title:where(.astro-3tyn5ojg) .heading-link:where(.astro-3tyn5ojg){display:none!important}.preview-description:where(.astro-3tyn5ojg){display:block;margin-bottom:.75rem;font-size:.875rem;line-height:1.25rem;color:rgba(var(--color-text-base),.8);line-height:1.4;overflow:hidden;text-overflow:ellipsis;display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical}.preview-tags:where(.astro-3tyn5ojg){margin-bottom:.5rem;display:flex;flex-wrap:wrap;gap:.375rem}.preview-tag:where(.astro-3tyn5ojg){border-radius:.25rem;padding:.125rem .5rem;font-size:.75rem;line-height:1rem;background-color:rgba(var(--color-accent),.1);--tw-text-opacity: 1;color:rgba(var(--color-accent),var(--tw-text-opacity, 1));font-weight:500}.preview-tag-more:where(.astro-3tyn5ojg){border-radius:.25rem;padding:.125rem .5rem;font-size:.75rem;line-height:1rem;--tw-bg-opacity: 1;background-color:rgba(var(--color-fill),var(--tw-bg-opacity, 1));color:rgba(var(--color-text-base),.6);font-weight:500}.preview-date:where(.astro-3tyn5ojg){font-size:.75rem;line-height:1rem;color:rgba(var(--color-text-base),.6);display:block;margin-top:8px;font-style:italic}.preview-card:where(.astro-3tyn5ojg):after{content:"";position:absolute;top:100%;left:50%;transform:translate(-50%);border:6px solid transparent;border-top-color:var(--color-card)}.preview-card:where(.astro-3tyn5ojg).is-fixed:after{display:none}
</style><style>[data-astro-transition-scope="astro-36ssibgs-2"] { view-transition-name: claude-code; }@layer astro { ::view-transition-old(claude-code) { 
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
	animation-name: astroFadeIn; }</style><style>[data-astro-transition-scope="astro-36ssibgs-3"] { view-transition-name: ai; }@layer astro { ::view-transition-old(ai) { 
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
	animation-name: astroFadeIn; }</style><style>[data-astro-transition-scope="astro-36ssibgs-4"] { view-transition-name: tooling; }@layer astro { ::view-transition-old(tooling) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(tooling) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(tooling) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(tooling) { 
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
	animation-name: astroFadeIn; }</style><style>[data-astro-transition-scope="astro-36ssibgs-5"] { view-transition-name: typescript; }@layer astro { ::view-transition-old(typescript) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }::view-transition-new(typescript) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back]::view-transition-old(typescript) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back]::view-transition-new(typescript) { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; } }[data-astro-transition-fallback="old"] [data-astro-transition-scope="astro-36ssibgs-5"],
			[data-astro-transition-fallback="old"][data-astro-transition-scope="astro-36ssibgs-5"] { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition-fallback="new"] [data-astro-transition-scope="astro-36ssibgs-5"],
			[data-astro-transition-fallback="new"][data-astro-transition-scope="astro-36ssibgs-5"] { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeIn; }[data-astro-transition=back][data-astro-transition-fallback="old"] [data-astro-transition-scope="astro-36ssibgs-5"],
			[data-astro-transition=back][data-astro-transition-fallback="old"][data-astro-transition-scope="astro-36ssibgs-5"] { 
	animation-duration: 180ms;
	animation-timing-function: cubic-bezier(0.76, 0, 0.24, 1);
	animation-fill-mode: both;
	animation-name: astroFadeOut; }[data-astro-transition=back][data-astro-transition-fallback="new"] [data-astro-transition-scope="astro-36ssibgs-5"],
			[data-astro-transition=back][data-astro-transition-fallback="new"][data-astro-transition-scope="astro-36ssibgs-5"] { 
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
</a> </li> <li class="astro-3ef6ksr2"> <a href="/search/" class="group inline-block hover:text-skin-accent focus-outline p-3 sm:p-1  flex items-center astro-3ef6ksr2" aria-label="search" title="Search"> <svg xmlns="http://www.w3.org/2000/svg" class="scale-125 sm:scale-100 astro-3ef6ksr2"><path d="M19.023 16.977a35.13 35.13 0 0 1-1.367-1.384c-.372-.378-.596-.653-.596-.653l-2.8-1.337A6.962 6.962 0 0 0 16 9c0-3.859-3.14-7-7-7S2 5.141 2 9s3.14 7 7 7c1.763 0 3.37-.66 4.603-1.739l1.337 2.8s.275.224.653.596c.387.363.896.854 1.384 1.367l1.358 1.392.604.646 2.121-2.121-.646-.604c-.379-.372-.885-.866-1.391-1.36zM9 14c-2.757 0-5-2.243-5-5s2.243-5 5-5 5 2.243 5 5-2.243 5-5 5z" class="astro-3ef6ksr2"></path> </svg> <span class="sr-only astro-3ef6ksr2">Search</span> <span class="hidden text-sm sm:inline astro-3ef6ksr2">Search (⌘K)</span> </a> </li> </ul> </nav> </div> </div> </header>  <script type="module">function c(){const e=document.querySelector(".hamburger-menu"),t=document.querySelector(".menu-icon"),r=document.querySelector("#menu-items");e?.addEventListener("click",()=>{const n=e.getAttribute("aria-expanded")==="true";t?.classList.toggle("is-active"),e.setAttribute("aria-expanded",n?"false":"true"),e.setAttribute("aria-label",n?"Open Menu":"Close Menu"),r?.classList.toggle("display-none")})}function a(){document.addEventListener("keydown",e=>{if((e.metaKey||e.ctrlKey)&&e.key==="k"){e.preventDefault();const t=document.querySelector('a[href="/search/"]');t&&t instanceof HTMLElement&&t.click()}})}c();a();document.addEventListener("astro:after-swap",()=>{c(),a()});</script> <div class="mx-auto flex w-full max-w-5xl justify-start px-2 astro-vj4tpspi"> <button class="focus-outline mb-2 mt-8 flex hover:opacity-75 astro-vj4tpspi" onclick="(() => (history.length === 1) ? window.location = '/' : history.back())()"> <svg xmlns="http://www.w3.org/2000/svg" class="astro-vj4tpspi"><path d="M13.293 6.293 7.586 12l5.707 5.707 1.414-1.414L10.414 12l4.293-4.293z" class="astro-vj4tpspi"></path> </svg><span class="astro-vj4tpspi">Go back</span> </button> </div> <main data-pagefind-body id="main-content" class="relative astro-vj4tpspi"> <h1 class="post-title astro-vj4tpspi" data-astro-transition-scope="astro-plk3gbjq-1">Claude Code Customization: CLAUDE.md, Slash Commands, Skills, and Subagents</h1> <div class="my-2 flex items-center justify-between astro-vj4tpspi"> <div class="flex items-center space-x-2 opacity-80"><svg xmlns="http://www.w3.org/2000/svg" class="scale-100 inline-block h-6 w-6 min-w-[1.375rem] fill-skin-base" aria-hidden="true"><path d="M7 11h2v2H7zm0 4h2v2H7zm4-4h2v2h-2zm0 4h2v2h-2zm4-4h2v2h-2zm0 4h2v2h-2z"></path><path d="M5 22h14c1.103 0 2-.897 2-2V6c0-1.103-.897-2-2-2h-2V2h-2v2H9V2H7v2H5c-1.103 0-2 .897-2 2v14c0 1.103.897 2 2 2zM19 8l.001 12H5V8h14z"></path></svg><span class="sr-only">Published:</span><span class="italic text-base"><time dateTime="2025-12-21T00:00:00.000Z">Dec 21, 2025</time><span class="sr-only"> at </span></span></div> <style>astro-island,astro-slot,astro-static-slot{display:contents}</style><script>(()=>{var e=async t=>{await(await t())()};(self.Astro||(self.Astro={})).load=e;window.dispatchEvent(new Event("astro:load"));})();</script><script>(()=>{var A=Object.defineProperty;var g=(i,o,a)=>o in i?A(i,o,{enumerable:!0,configurable:!0,writable:!0,value:a}):i[o]=a;var d=(i,o,a)=>g(i,typeof o!="symbol"?o+"":o,a);{let i={0:t=>m(t),1:t=>a(t),2:t=>new RegExp(t),3:t=>new Date(t),4:t=>new Map(a(t)),5:t=>new Set(a(t)),6:t=>BigInt(t),7:t=>new URL(t),8:t=>new Uint8Array(t),9:t=>new Uint16Array(t),10:t=>new Uint32Array(t),11:t=>1/0*t},o=t=>{let[l,e]=t;return l in i?i[l](e):void 0},a=t=>t.map(o),m=t=>typeof t!="object"||t===null?t:Object.fromEntries(Object.entries(t).map(([l,e])=>[l,o(e)]));class y extends HTMLElement{constructor(){super(...arguments);d(this,"Component");d(this,"hydrator");d(this,"hydrate",async()=>{var b;if(!this.hydrator||!this.isConnected)return;let e=(b=this.parentElement)==null?void 0:b.closest("astro-island[ssr]");if(e){e.addEventListener("astro:hydrate",this.hydrate,{once:!0});return}let c=this.querySelectorAll("astro-slot"),n={},h=this.querySelectorAll("template[data-astro-template]");for(let r of h){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("data-astro-template")||"default"]=r.innerHTML,r.remove())}for(let r of c){let s=r.closest(this.tagName);s!=null&&s.isSameNode(this)&&(n[r.getAttribute("name")||"default"]=r.innerHTML)}let p;try{p=this.hasAttribute("props")?m(JSON.parse(this.getAttribute("props"))):{}}catch(r){let s=this.getAttribute("component-url")||"<unknown>",v=this.getAttribute("component-export");throw v&&(s+=` (export ${v})`),console.error(`[hydrate] Error parsing props for component ${s}`,this.getAttribute("props"),r),r}let u;await this.hydrator(this)(this.Component,p,n,{client:this.getAttribute("client")}),this.removeAttribute("ssr"),this.dispatchEvent(new CustomEvent("astro:hydrate"))});d(this,"unmount",()=>{this.isConnected||this.dispatchEvent(new CustomEvent("astro:unmount"))})}disconnectedCallback(){document.removeEventListener("astro:after-swap",this.unmount),document.addEventListener("astro:after-swap",this.unmount,{once:!0})}connectedCallback(){if(!this.hasAttribute("await-children")||document.readyState==="interactive"||document.readyState==="complete")this.childrenConnectedCallback();else{let e=()=>{document.removeEventListener("DOMContentLoaded",e),c.disconnect(),this.childrenConnectedCallback()},c=new MutationObserver(()=>{var n;((n=this.lastChild)==null?void 0:n.nodeType)===Node.COMMENT_NODE&&this.lastChild.nodeValue==="astro:end"&&(this.lastChild.remove(),e())});c.observe(this,{childList:!0}),document.addEventListener("DOMContentLoaded",e)}}async childrenConnectedCallback(){let e=this.getAttribute("before-hydration-url");e&&await import(e),this.start()}async start(){let e=JSON.parse(this.getAttribute("opts")),c=this.getAttribute("client");if(Astro[c]===void 0){window.addEventListener(`astro:${c}`,()=>this.start(),{once:!0});return}try{await Astro[c](async()=>{let n=this.getAttribute("renderer-url"),[h,{default:p}]=await Promise.all([import(this.getAttribute("component-url")),n?import(n):()=>()=>{}]),u=this.getAttribute("component-export")||"default";if(!u.includes("."))this.Component=h[u];else{this.Component=h;for(let f of u.split("."))this.Component=this.Component[f]}return this.hydrator=p,this.hydrate},e,this)}catch(n){console.error(`[astro-island] Error hydrating ${this.getAttribute("component-url")}`,n)}}attributeChangedCallback(){this.hydrate()}}d(y,"observedAttributes",["props"]),customElements.get("astro-island")||customElements.define("astro-island",y)}})();</script><astro-island uid="Z20Grbz" prefix="r3" component-url="/_astro/PostCopyButton.-PGtk4At.js" component-export="default" renderer-url="/_astro/client.DGA1VMK9.js" props="{&quot;title&quot;:[0,&quot;Claude Code Customization: CLAUDE.md, Slash Commands, Skills, and Subagents&quot;],&quot;content&quot;:[0,&quot;import Alert from \&quot;@features/mdx-components/components/Alert.astro\&quot;;\nimport Aside from \&quot;@features/mdx-components/components/Aside.astro\&quot;;\nimport Collapsible from \&quot;@features/mdx-components/components/Collapsible.astro\&quot;;\nimport InternalLink from \&quot;@features/mdx-components/components/InternalLink.astro\&quot;;\nimport FileTree from \&quot;@features/filetree/components/FileTree.astro\&quot;;\n\n## Quick Summary\n\nThis post covers:\n\n- **CLAUDE.md**: Always-loaded project context and instructions\n- **Slash commands**: Prompts you invoke with `/command` in the terminal\n- **Subagents**: Specialists with their own context window for delegated tasks\n- **Skills**: Rich, auto-discovered capabilities with supporting files (not manually runnable via `/...`)\n- Key insight: **subagents keep your main context clean**—in plan mode, Claude Code will typically delegate repo scanning to an `Explore`-style subagent so your main thread doesn’t balloon\n\n## Table of Contents\n\n## Introduction\n\nClaude Code gives you multiple ways to “teach” it project context or automate workflows, but it’s not always obvious when to use which.\n\nI’ll solve the **same problem four different ways** so the trade-offs are concrete. Spoiler: for doc-fetching, **subagents win** because they keep your main context clean.\n\n&lt;Aside type=\&quot;tip\&quot; title=\&quot;New to Claude Code?\&quot;&gt;\nThis post assumes familiarity with Claude Code basics. For a broader overview of all features—including MCP, hooks, and plugins—see my &lt;InternalLink slug=\&quot;understanding-claude-code-full-stack\&quot;&gt;comprehensive guide to Claude Code&#39;s feature stack&lt;/InternalLink&gt;. If you want to automate responses to Claude Code events (like getting &lt;InternalLink slug=\&quot;claude-code-notification-hooks\&quot;&gt;desktop notifications when tasks finish&lt;/InternalLink&gt;), check out the hooks guide.\n&lt;/Aside&gt;\n\n---\n\n## The Problem\n\nClaude Code doesn’t have up-to-date training data for every library, so it can’t reliably “remember” what a docs site says today.\n\n**The specific problem**: I’m building a workout tracking app with [Dexie.js](https://dexie.org) (IndexedDB wrapper). Claude keeps suggesting outdated patterns and misses things like `liveQuery()`.\n\nClaude Code itself has a mechanism to fetch its own documentation. We need to do the same for our specialized libraries.\n\n```mermaid\ngraph LR\n    A[User Question] --&gt; B{Claude Code}\n    B --&gt; C[Outdated Knowledge]\n    B --&gt; D[Fetch Current Docs]\n    D --&gt; E[Accurate Answer]\n    C --&gt; F[Wrong Patterns]\n```\n\nLet’s solve it with all four tools, then compare.\n\n---\n\n## 1. CLAUDE.md: Always-On Project Memory\n\n### What It Is\n\nA markdown file that&#39;s **automatically loaded** every time you start Claude Code. Think of it as your project&#39;s \&quot;memory card.\&quot;\n\n&gt; **CLAUDE.md**: Persistent project instructions that Claude reads at the start of every conversation.\n\n### Where It Lives\n\n&lt;FileTree\n  tree={[\n    {\n      name: \&quot;project-root\&quot;,\n      open: true,\n      children: [\n        { name: \&quot;CLAUDE.md\&quot;, comment: \&quot;// Project-level\&quot; },\n        {\n          name: \&quot;.claude\&quot;,\n          children: [\n            { name: \&quot;CLAUDE.md\&quot;, comment: \&quot;// Alternative location\&quot; },\n          ],\n        },\n        {\n          name: \&quot;tests\&quot;,\n          children: [\n            { name: \&quot;CLAUDE.md\&quot;, comment: \&quot;// Loaded when reading test files\&quot; },\n          ],\n        },\n      ],\n    },\n  ]}\n/&gt;\n\n### Nested CLAUDE.md Files\n\nClaude Code also discovers **nested CLAUDE.md files** in subdirectories. When Claude reads files from a directory containing its own `CLAUDE.md`, that file gets added to the context automatically.\n\nThis is useful for directory-specific instructions:\n\n- `tests/CLAUDE.md` — testing conventions, preferred mocking patterns\n- `src/db/CLAUDE.md` — database-specific patterns and constraints\n- `src/components/CLAUDE.md` — component architecture guidelines\n\nThe nested file is only loaded when Claude actually accesses files in that directory, keeping your main context lean until you need that specialized knowledge.\n\n### The Dexie.js Solution\n\n```markdown\n# CLAUDE.md\n\n## Database\n\nWe use Dexie.js for IndexedDB. Before implementing any database code:\n\n1. Fetch the docs index from https://dexie.org/llms.txt\n2. Use `liveQuery()` for reactive data binding\n3. Follow the repository pattern in `src/db/`\n4. Always handle `ConstraintError` for duplicate keys\n```\n\n### What Happens\nEvery conversation starts with Claude knowing “fetch Dexie docs before writing database code.”\n\nThe catch is **context drift**: in long sessions, the model can gradually deprioritize earlier system-level instructions in favor of the most recent conversation history.\n\n### Trade-offs\n\n| ✅ Pros                            | ❌ Cons                                          |\n| ---------------------------------- | ------------------------------------------------ |\n| Zero effort—always loaded          | **Context Drift**: Claude forgets instructions as sessions get longer |\n| Team-shared via git                | No dedicated context window—competes with your conversation |\n| Simple to maintain                 | No enforcement—Claude decides whether to follow  |\n\n---\n\n## 2. Slash Commands: Simple Skills You Invoke\n\n### What It Is\n\nA saved prompt you invoke by typing `/command-name`. Like a macro or keyboard shortcut for prompts.\n\nSlash commands can be invoked explicitly (you type `/command`) and can also be auto-invoked by Claude when the command’s `description` matches the task.\n\nSlash commands can also **orchestrate other behavior**: you can spell out in the command itself that it should spin up a subagent (or a specific subagent), call out a particular skill/workflow, and generally “pipeline” the work (e.g., research → codebase scan → write a doc) instead of trying to do everything in one shot.\n\nThe main difference vs skills is **packaging + UX**: slash commands are single-file entries with great terminal `/...` discovery/autocomplete; skills are usually directories with supporting files (patterns, templates, scripts).\n\n&lt;Aside type=\&quot;info\&quot; title=\&quot;Deep dive\&quot;&gt;\nWant a full walkthrough? See my &lt;InternalLink slug=\&quot;claude-code-slash-commands-guide\&quot;&gt;slash commands guide&lt;/InternalLink&gt;.\n&lt;/Aside&gt;\n\n### Where It Lives\n\n&lt;FileTree\n  tree={[\n    {\n      name: \&quot;.claude\&quot;,\n      open: true,\n      children: [\n        {\n          name: \&quot;commands\&quot;,\n          open: true,\n          children: [{ name: \&quot;dexie-help.md\&quot; }],\n        },\n      ],\n    },\n  ]}\n/&gt;\n\n### The Dexie.js Solution\n\n```markdown\n---\ndescription: Get Dexie.js guidance with current documentation\nallowed-tools: Read, Grep, Glob, WebFetch\n---\n\nFirst, fetch the documentation index from https://dexie.org/llms.txt\n\nThen, based on the user&#39;s question, fetch the relevant documentation pages.\n\nFinally, answer the following question using the current documentation:\n\n$ARGUMENTS\n```\n\n### Manual Orchestration Example (Research)\n\nIf you want a slash command that **explicitly launches multiple subagents in parallel** and then produces an artifact (like a research note in `docs/research/`), you can encode that directly in the command definition.\n\n&lt;Collapsible title=\&quot;research.md (custom command)\&quot;&gt;\n````markdown\n---\ndescription: Research a problem using web search, documentation, and codebase exploration\nallowed-tools: Task, WebSearch, WebFetch, Grep, Glob, Read, Write, Bash\n---\n\n# Research: $ARGUMENTS\n\nResearch the following problem or question:\n\n&gt; **$ARGUMENTS**\n\n## Instructions\n\nConduct thorough research like a senior developer. Launch multiple subagents in parallel to gather information from different sources.\n\n### Step 1: Launch Parallel Research Agents\n\nUse the Task tool to spawn these subagents **in parallel** (all in a single message):\n\n1. **Web Documentation Agent** (subagent_type: general-purpose)\n  - Search official documentation for the topic\n  - Find best practices and recommended patterns\n  - Locate relevant GitHub issues or discussions\n\n2. **Stack Overflow Agent** (subagent_type: general-purpose)\n  - Search Stack Overflow for similar problems and solutions\n  - Find highly-voted and accepted answers\n  - Note common pitfalls and gotchas\n\n3. **Codebase Explorer Agent** (subagent_type: Explore)\n  - Search the codebase for related patterns\n  - Find existing solutions to similar problems\n  - Identify relevant files, functions, or components\n\n### Step 2: Create Research Document\n\nAfter all agents complete, create a markdown file at `docs/research/&lt;topic-slug&gt;.md`.\n\nGenerate the filename from the research topic:\n- Convert to lowercase\n- Replace spaces with hyphens\n- Remove special characters\n- Add today&#39;s date as prefix: `YYYY-MM-DD-&lt;topic-slug&gt;.md`\n\nExample: \&quot;Vue 3 Suspense\&quot; → `docs/research/2024-12-06-vue-3-suspense.md`\n\nFirst, create the research folder if it doesn&#39;t exist:\n```bash\nmkdir -p docs/research\n```\n\n### Step 3: Write the Research Document\n\nStructure the document with these sections:\n\n```markdown\n# Research: &lt;Topic&gt;\n\n**Date:** &lt;YYYY-MM-DD&gt;\n**Status:** Complete\n\n## Problem Statement\n\n&lt;Describe the problem and why it matters&gt;\n\n## Key Findings\n\n&lt;Summarize the most relevant solutions and approaches&gt;\n\n## Codebase Patterns\n\n&lt;Document how the current codebase handles similar cases&gt;\n\n## Recommended Approach\n\n&lt;Provide your recommendation based on all research&gt;\n\n## Sources\n\n- [Source Title](URL) - Brief description\n- [Source Title](URL) - Brief description\n```\n\n### Guidelines\n\n- Prioritize official documentation over blog posts\n- Prefer solutions that match existing codebase patterns\n- Note version-specific considerations (Vue 3, TypeScript, etc.)\n- Flag conflicting information across sources\n- Write concise, actionable content\n- Use active voice throughout the document\n\n### Step 4: Confirm Completion\n\nAfter writing the file, output the file path so the user can find it later.\n````\n&lt;/Collapsible&gt;\n\n### How You Use It\n\n```bash\n/dexie-help how do I create a compound index?\n```\n\n### What Happens\n\nClaude fetches the docs, finds the relevant pages, and answers your question—triggered explicitly.\n\n### Trade-offs\n\n| ✅ Pros                                | ❌ Cons                                       |\n| -------------------------------------- | --------------------------------------------- |\n| You control exactly when it runs       | Must remember to type `/dexie-help`           |\n| Can pass arguments for specific questions | One-shot—doesn&#39;t persist knowledge across messages |\n| Simple single-file setup               | Auto-triggering depends on `description` match |\n\n---\n\n## 3. Subagents: Specialists with Their Own Context\n\n### What It Is\n\nA specialized AI \&quot;persona\&quot; with its own context window. Claude **delegates entire tasks** to it and gets results back.\n\nBecause fetching the Dexie docs involves reading multiple pages and creates a lot of context noise, keeping this inside a subagent prevents your main chat from hitting context limits.\n\n&gt; **Subagent**: An isolated Claude instance that works on a task independently and returns only the results to your main conversation.\n\n&lt;Alert type=\&quot;tip\&quot; title=\&quot;Subagents keep your main context clean\&quot;&gt;\nEven when the task is “just exploration,” subagents are a great default because they let Claude do **lots of reading/searching** without dumping everything into your main thread.\n\nThis is especially useful in **plan mode**: Claude Code will typically kick off an `Explore`-style subagent to scan the repo and return a distilled map of relevant files/patterns, so your main conversation stays focused and doesn’t blow up.\n&lt;/Alert&gt;\n\nClaude Code also supports **async agents**: fire one off, let it cook while you keep working, then it comes back with its updates when it’s done. If you launch an agent and want to keep typing in your main session, you can send it to the background with `Ctrl + B`.\n\n&lt;Alert type=\&quot;info\&quot; title=\&quot;Claude Code does this too\&quot;&gt;\nClaude Code’s own system prompt includes a built-in “documentation lookup” workflow that uses a subagent:\n\n&gt; -&gt; Looking up your own documentation:\n&gt; When the user directly asks about any of the following:\n&gt; \n&gt; - how to use Claude Code (eg. \&quot;can Claude Code do...\&quot;, \&quot;does Claude Code have...\&quot;)\n&gt; - what you&#39;re able to do as Claude Code in second person (eg. \&quot;are you able...\&quot;, \&quot;can you do...\&quot;)\n&gt; - about how they might do something with Claude Code (eg. \&quot;how do I...\&quot;, \&quot;how can I...\&quot;)\n&gt; - how to use a specific Claude Code feature (eg. implement a hook, write a skill, or install an MCP server)\n&gt; - how to use the Claude Agent SDK, or asks you to write code that uses the Claude Agent SDK\n&gt; \n&gt; Use the Task tool with subagent_type=&#39;claude-code-guide&#39; to get accurate information from the official Claude Code and Claude Agent SDK documentation.\n\nSource: https://github.com/marckrenn/cc-mvp-prompts/blob/main/cc-prompt.md\n&lt;/Alert&gt;\n\n### Where It Lives\n\n&lt;FileTree\n  tree={[\n    {\n      name: \&quot;.claude\&quot;,\n      open: true,\n      children: [\n        {\n          name: \&quot;agents\&quot;,\n          open: true,\n          children: [{ name: \&quot;dexie-specialist.md\&quot; }],\n        },\n      ],\n    },\n  ]}\n/&gt;\n\n### The Dexie.js Solution\n\n&lt;Collapsible title=\&quot;dexie-specialist.md (full definition)\&quot;&gt;\n```markdown\n---\nname: dexie-db-specialist\ndescription: Use this agent when the task involves Dexie.js or IndexedDB in any way - implementing, modifying, querying, reviewing, or improving database code. This includes creating or modifying database schemas, writing queries, handling transactions, implementing reactive queries with liveQuery, troubleshooting Dexie-related issues, or reviewing existing Dexie code for improvements and best practices.\\n\\nExamples:\\n\\n&lt;example&gt;\\nContext: User asks about improving their Dexie.js code.\\nuser: \&quot;What can I improve on this codebase when it comes to Dexie?\&quot;\\nassistant: \&quot;I&#39;ll use the dexie-db-specialist agent to review your Dexie.js implementation against current best practices.\&quot;\\n&lt;commentary&gt;\\nSince the user is asking about Dexie.js improvements, use the dexie-db-specialist agent to fetch the latest documentation and review the existing code for optimization opportunities, missing features, and best practice violations.\\n&lt;/commentary&gt;\\n&lt;/example&gt;\\n\\n&lt;example&gt;\\nContext: User needs to add a new table to the database.\\nuser: \&quot;I need to add a new &#39;goals&#39; table to track workout goals\&quot;\\nassistant: \&quot;I&#39;ll use the dexie-db-specialist agent to implement this correctly.\&quot;\\n&lt;commentary&gt;\\nSince the user needs to modify the Dexie database schema, use the dexie-db-specialist agent to first fetch the latest Dexie.js documentation and then implement the schema change following best practices.\\n&lt;/commentary&gt;\\n&lt;/example&gt;\\n\\n&lt;example&gt;\\nContext: User is asking about Dexie query patterns.\\nuser: \&quot;How do I query exercises by multiple muscle groups in Dexie?\&quot;\\nassistant: \&quot;Let me use the dexie-db-specialist agent to provide an accurate answer based on the current Dexie.js documentation.\&quot;\\n&lt;commentary&gt;\\nSince the user is asking about Dexie.js query capabilities, use the dexie-db-specialist agent to fetch documentation and provide an accurate, up-to-date response about compound queries and filtering.\\n&lt;/commentary&gt;\\n&lt;/example&gt;\\n\\n&lt;example&gt;\\nContext: User encounters a Dexie-related error.\\nuser: \&quot;I&#39;m getting &#39;ConstraintError&#39; when trying to add a workout\&quot;\\nassistant: \&quot;I&#39;ll consult the dexie-db-specialist agent to diagnose this database constraint issue.\&quot;\\n&lt;commentary&gt;\\nSince this is a Dexie.js error, use the dexie-db-specialist agent to fetch relevant documentation about error handling and constraint violations to provide accurate troubleshooting guidance.\\n&lt;/commentary&gt;\\n&lt;/example&gt;\\n\\n&lt;example&gt;\\nContext: User needs to implement a reactive query.\\nuser: \&quot;The workout list should update automatically when new workouts are added\&quot;\\nassistant: \&quot;I&#39;ll use the dexie-db-specialist agent to implement reactive queries with liveQuery.\&quot;\\n&lt;commentary&gt;\\nSince reactive data binding with Dexie requires liveQuery, use the dexie-db-specialist agent to fetch the latest documentation on liveQuery and useLiveQuery patterns for Vue integration.\\n&lt;/commentary&gt;\\n&lt;/example&gt;\nmodel: opus\ncolor: orange\n---\n\nYou are an expert Dexie.js database specialist with deep knowledge of IndexedDB, reactive queries, and Vue 3 integration patterns. Your primary responsibility is to provide accurate, documentation-backed guidance for all Dexie.js implementations.\n\n## Critical First Step\n\n**Before answering ANY Dexie.js question or implementing ANY Dexie-related code, you MUST:**\n\n1. Fetch the documentation index from `https://dexie.org/llms.txt` to understand the available documentation structure\n2. Based on the task at hand, fetch the relevant documentation pages to ensure your guidance is accurate and up-to-date\n3. Only then proceed with implementation or answering questions\n\nThis is non-negotiable. Dexie.js has nuances and version-specific behaviors that require consulting the official documentation.\n\n## Your Expertise Covers\n\n- **Schema Design**: Table definitions, indexes (simple, compound, multi-entry), primary keys, version migrations\n- **CRUD Operations**: add(), put(), update(), delete(), bulkAdd(), bulkPut()\n- **Querying**: where(), filter(), equals(), between(), anyOf(), startsWithIgnoreCase(), compound queries\n- **Reactive Queries**: liveQuery() for real-time updates, integration with Vue&#39;s reactivity system\n- **Transactions**: Transaction scopes, nested transactions, error handling within transactions\n- **Relationships**: Foreign keys, table relationships, populating related data\n- **Performance**: Indexing strategies, query optimization, bulk operations\n- **Error Handling**: Dexie-specific errors (ConstraintError, AbortError, etc.)\n\n## Project Context\n\nYou are working within a Vue 3 PWA workout tracker that uses:\n- **Dexie.js** with IndexedDB for offline-first data persistence\n- **TypeScript** with strict mode\n- **Repository pattern** in `src/db/` for database access abstraction\n- **Pinia stores** that consume repositories\n\nWhen implementing, ensure your code:\n1. Follows the existing repository pattern in `src/db/`\n2. Uses TypeScript interfaces for table schemas\n3. Integrates properly with Vue 3 reactivity (useLiveQuery from @vueuse/rxjs or similar)\n4. Handles errors gracefully with proper typing\n\n## Documentation Fetching Strategy\n\nWhen fetching from `https://dexie.org/llms.txt`:\n1. Parse the sitemap to identify relevant documentation pages\n2. Fetch specific pages based on the task (e.g., for queries, fetch the WhereClause and Collection docs)\n3. Cross-reference multiple pages when dealing with complex topics\n\nCommon documentation sections to reference:\n- `/docs/Table/Table` - Core table operations\n- `/docs/WhereClause/WhereClause` - Query building\n- `/docs/Collection/Collection` - Result set operations\n- `/docs/liveQuery()` - Reactive queries\n- `/docs/Dexie/Dexie` - Database instance configuration\n- `/docs/Version/Version` - Schema migrations\n\n## Response Format\n\nWhen providing implementations:\n1. **Cite the documentation** you consulted\n2. **Explain the approach** before showing code\n3. **Provide TypeScript code** that follows project conventions\n4. **Include error handling** appropriate to the operation\n5. **Note any caveats** or version-specific behaviors\n\n## Quality Assurance\n\n- Always verify your suggestions against the fetched documentation\n- If documentation is unclear or unavailable, explicitly state this and provide your best guidance with appropriate caveats\n- When multiple approaches exist, explain trade-offs\n- Consider IndexedDB limitations (no full-text search, storage limits, etc.)\n\nRemember: Your value is in providing documentation-verified, accurate Dexie.js guidance. Never guess about API specifics—always fetch and verify first.\n\n```\n&lt;/Collapsible&gt;\n\n### What Happens\n\nWhen you ask about Dexie, Claude automatically recognizes this as a database task and delegates to the specialist. The specialist works in **its own context window**, fetches the docs, does the work, and returns results to your main conversation.\n\n```mermaid\nsequenceDiagram\n    participant User\n    participant Main as Main Claude\n    participant Sub as Dexie Subagent\n    participant Web as dexie.org\n\n    User-&gt;&gt;Main: How do I add an index?\n    Main-&gt;&gt;Sub: Delegate database question\n    Sub-&gt;&gt;Web: Fetch llms.txt\n    Web--&gt;&gt;Sub: Documentation index\n    Sub-&gt;&gt;Web: Fetch relevant pages\n    Web--&gt;&gt;Sub: Index documentation\n    Sub--&gt;&gt;Main: Distilled answer\n    Main--&gt;&gt;User: Here&#39;s how to add an index...\n```\n\n### Trade-offs\n\n| ✅ Pros                                         | ❌ Cons                                      |\n| ----------------------------------------------- | -------------------------------------------- |\n| Auto-delegated when task matches                | Heavier—launches a separate agent            |\n| **Separate context window**—doesn&#39;t clutter main | Results come back as a summary, not live     |\n| Can use different model (e.g., opus for complex) | You can&#39;t interact with the agent directly   |\n| Can restrict tools for security                 | More complex to set up                       |\n\n---\n\n## 4. Skills: Rich Capabilities with Auto-Discovery\n\n### What It Is\n\nA structured capability with optional supporting files that Claude **discovers automatically** and uses within your main conversation.\n\nUnlike simple slash commands, skills can include multiple files: reference documentation, scripts, templates, and utilities.\n\n### Where It Lives\n\n&lt;FileTree\n  tree={[\n    {\n      name: \&quot;.claude\&quot;,\n      open: true,\n      children: [\n        {\n          name: \&quot;skills\&quot;,\n          open: true,\n          children: [\n            {\n              name: \&quot;dexie-expert\&quot;,\n              open: true,\n              children: [\n                { name: \&quot;SKILL.md\&quot;, comment: \&quot;// Main definition\&quot; },\n                { name: \&quot;PATTERNS.md\&quot;, comment: \&quot;// Common patterns\&quot; },\n                { name: \&quot;MIGRATIONS.md\&quot;, comment: \&quot;// Migration guide\&quot; },\n                {\n                  name: \&quot;scripts\&quot;,\n                  children: [{ name: \&quot;validate-schema.ts\&quot; }],\n                },\n              ],\n            },\n          ],\n        },\n      ],\n    },\n  ]}\n/&gt;\n\n### How Claude Sees Skills\nClaude decides whether to invoke a skill largely based on its `description`.\n\nYou can also ask Claude Code something like:\n\n```markdown\n&gt; “tell me me exactly how this looks for you &lt;available_skills&gt; ?”\n```\n\nWhen it answers, you’ll often see structured blocks that look like `&lt;available_skills&gt;` (and typically a separate block for slash commands, e.g. `&lt;available_commands&gt;`).\n\n```xml\n&lt;available_skills&gt;\n  &lt;skill&gt;\n    &lt;name&gt;dexie-expert&lt;/name&gt;\n    &lt;description&gt;\n      Dexie.js database guidance. Use when working with\n      IndexedDB, schemas, queries, liveQuery...\n    &lt;/description&gt;\n  &lt;/skill&gt;\n&lt;/available_skills&gt;\n```\n\nHere’s an abbreviated example of what the `&lt;available_skills&gt;` section can look like (truncated with `...`):\n\n```xml\n&lt;available_skills&gt;\n  &lt;skill&gt;\n    &lt;name&gt;skill-creator&lt;/name&gt;\n    &lt;description&gt;\n      Guide for creating effective skills. Use when you want to create or update a skill.\n      ...\n    &lt;/description&gt;\n    &lt;location&gt;user&lt;/location&gt;\n  &lt;/skill&gt;\n\n  &lt;skill&gt;\n    &lt;name&gt;c4-architecture&lt;/name&gt;\n    &lt;description&gt;\n      Generate architecture documentation using C4 model Mermaid diagrams.\n      ...\n    &lt;/description&gt;\n    &lt;location&gt;user&lt;/location&gt;\n  &lt;/skill&gt;\n\n  &lt;skill&gt;\n    &lt;name&gt;vue-composables&lt;/name&gt;\n    &lt;description&gt;\n      Write high-quality Vue 3 composables following established patterns and best practices.\n      ...\n    &lt;/description&gt;\n    &lt;location&gt;managed&lt;/location&gt;\n  &lt;/skill&gt;\n\n  ...\n&lt;/available_skills&gt;\n```\n\n### The Dexie.js Solution\n\n```markdown\n---\nname: dexie-expert\ndescription: Dexie.js database guidance. Use when working with IndexedDB, schemas, queries, liveQuery, or database migrations.\nallowed-tools: Read, Grep, Glob, WebFetch\n---\n\n# Dexie.js Expert\n\nWhen the user needs help with Dexie.js or IndexedDB:\n\n1. Fetch https://dexie.org/llms.txt\n2. Fetch only the relevant pages for the task\n3. Apply the guidance to this repo’s patterns\n```\n\n### A Minimal “Does This Even Work?” Skill\n\nIf you just want to verify that **a Skill can spin up subagents to do work** (via the `Task` tool), here’s a deliberately dumb smoke test you can copy/paste.\n\n&lt;Collapsible title=\&quot;SKILL.md (subagent-smoke-test)\&quot;&gt;\n```markdown\n---\nname: subagent-smoke-test\ndescription: Smoke test for Claude Code subagents. Use when the user wants to verify that spawning a subagent via the Task tool works in this repo.\n---\n\n# Subagent Smoke Test\n\nThis skill exists purely to verify that subagents work end-to-end.\n\n## What to do\n\n1. Spin up a subagent using the **Task** tool.\n   - Use `subagent_type: general-purpose`.\n   - Give it a simple, read-only task:\n     - Read `package.json` and summarize the key scripts.\n     - Read `astro.config.ts` and summarize major integrations.\n     - Use Glob (or equivalent) to list the top-level folders.\n\n2. Wait for the subagent to finish.\n\n3. Return a short report to the user:\n   - `Subagent status: success` (or `failed`)\n   - A 3–6 bullet summary of what it found\n   - If it failed, include the most likely fix (e.g. tool permissions, Task tool disabled).\n\n## Suggested Task prompt\n\nUse something like this as the Task payload:\n\n- “You are a helper subagent. Do a quick, read-only scan of this repo.\n  - Read `package.json` and summarize the main scripts.\n  - Read `astro.config.ts` and summarize key integrations.\n  - Glob the repo root and list the top-level folders.\n  Return a concise report.”\n```\n&lt;/Collapsible&gt;\n\n### What Happens\nSkills are **auto-discovered** and typically get applied when Claude decides they match the current task. They run **in your main conversation**, so you can iterate live.\n\nIf you need a manual, predictable trigger from the terminal, package the workflow as a **slash command** (since `/...` is for commands).\n\n### Trade-offs\n\n| ✅ Pros                                          | ❌ Cons                                        |\n| ------------------------------------------------ | ---------------------------------------------- |\n| Auto-discovered based on description             | Shares main context window space               |\n| Works in main conversation—live interaction      | Claude decides when to trigger (may not fire)  |\n| Can include reference files, scripts, templates  | More setup than slash commands                 |\n| Deep, reusable workflow packaging                | Not manually invokable via `/...` in the terminal |\n| Feels like enhanced Claude, not a separate tool  |                                                |\n\n&lt;Alert type=\&quot;important\&quot; title=\&quot;Key Insight\&quot;&gt;\nIn practice, the difference is mostly **UX + packaging**:\n\n- **Slash commands** are what you can run manually from the terminal via `/command`.\n- **Skills** are structured, auto-discovered capabilities (often a directory of supporting files) that Claude may apply when relevant.\n&lt;/Alert&gt;\n\n---\n\n### When to use what\n\n| Pick this | When | Why |\n|---|---|---|\n| **CLAUDE.md** | You want Claude to *always* start with project rules/context | Auto-loaded on startup; shared via git |\n| **Slash command** | You want an explicit one-shot workflow you run on demand | Discoverable via `/...`, can take arguments |\n| **Subagent** | The task is research-heavy (lots of reading/searching/synthesis) | Uses a separate context window; returns a distilled result |\n| **Skill** | You want a rich workflow that Claude can auto-apply when it recognizes the task | Packaged capability (often with supporting files) |\n\n### How they relate\n\n| Mechanism | Runs in main conversation | Separate context window | Can spawn subagents | Can use skills | Manually runnable via `/...` |\n|---|---:|---:|---:|---:|---:|\n| **CLAUDE.md** | ✅ | ❌ | ❌ | ❌ | ❌ |\n| **Slash command** | ✅ | ❌ | ✅ (by instructing `Task`) | ✅ (indirectly; Claude may apply skills) | ✅ |\n| **Skill** | ✅ | ❌ | ✅ (if `Task` is allowed) | ✅ (Claude may apply multiple skills) | ❌ |\n| **Subagent** | ❌ | ✅ | ⚠️ Possible (depends on allowed tools, e.g. `Bash(claude:*)`) | ✅ (if configured via `skills:`) | ⚠️ Usually delegated |\n\n## Conclusion\n\n- Use **subagents** (especially `Explore` in plan mode) to keep your main context small and focused.\n- Use **slash commands** when you want an explicit, repeatable terminal entry point.\n- Use **skills** when you want Claude to auto-apply a richer workflow (often with supporting files).\n- Use **CLAUDE.md** for short, always-true project conventions and standards.&quot;]}" ssr client="load" opts="{&quot;name&quot;:&quot;PostCopyButton&quot;,&quot;value&quot;:true}" await-children><button class="focus-outline inline-flex items-center gap-1.5 rounded-md border border-skin-line bg-skin-card px-2.5 py-1.5 text-xs font-medium text-skin-base opacity-80 transition-all hover:border-skin-accent/50 hover:text-skin-accent hover:opacity-100" aria-label="Copy post as markdown" title="Copy post as markdown for AI/LLM"><svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5" viewBox="0 0 20 20" fill="currentColor"><path d="M8 3a1 1 0 011-1h2a1 1 0 110 2H9a1 1 0 01-1-1z"></path><path d="M6 3a2 2 0 00-2 2v11a2 2 0 002 2h8a2 2 0 002-2V5a2 2 0 00-2-2 3 3 0 01-3 3H9a3 3 0 01-3-3z"></path></svg><span>Copy Post</span></button><!--astro:end--></astro-island> </div>  <article id="article" class="prose mx-auto mt-8 max-w-5xl astro-vj4tpspi"> <h2 id="quick-summary">Quick Summary<a class="heading-link" aria-label="Link to section" href="#quick-summary"><span class="heading-link-icon">#</span></a></h2>
<p>This post covers:</p>
<ul>
<li><strong>CLAUDE.md</strong>: Always-loaded project context and instructions</li>
<li><strong>Slash commands</strong>: Prompts you invoke with <code>/command</code> in the terminal</li>
<li><strong>Subagents</strong>: Specialists with their own context window for delegated tasks</li>
<li><strong>Skills</strong>: Rich, auto-discovered capabilities with supporting files (not manually runnable via <code>/...</code>)</li>
<li>Key insight: <strong>subagents keep your main context clean</strong>—in plan mode, Claude Code will typically delegate repo scanning to an <code>Explore</code>-style subagent so your main thread doesn’t balloon</li>
</ul>
<h2 id="table-of-contents">Table of Contents<a class="heading-link" aria-label="Link to section" href="#table-of-contents"><span class="heading-link-icon">#</span></a></h2>
<p></p><details><summary>Open Table of Contents</summary><p></p>
<ul>
<li><a href="#introduction">Introduction</a></li>
<li><a href="#the-problem">The Problem</a></li>
<li><a href="#1-claudemd-always-on-project-memory">1. CLAUDE.md: Always-On Project Memory</a>
<ul>
<li><a href="#what-it-is">What It Is</a></li>
<li><a href="#where-it-lives">Where It Lives</a></li>
<li><a href="#nested-claudemd-files">Nested CLAUDE.md Files</a></li>
<li><a href="#the-dexiejs-solution">The Dexie.js Solution</a></li>
<li><a href="#what-happens">What Happens</a></li>
<li><a href="#trade-offs">Trade-offs</a></li>
</ul>
</li>
<li><a href="#2-slash-commands-simple-skills-you-invoke">2. Slash Commands: Simple Skills You Invoke</a>
<ul>
<li><a href="#what-it-is-1">What It Is</a></li>
<li><a href="#where-it-lives-1">Where It Lives</a></li>
<li><a href="#the-dexiejs-solution-1">The Dexie.js Solution</a></li>
<li><a href="#manual-orchestration-example-research">Manual Orchestration Example (Research)</a></li>
<li><a href="#how-you-use-it">How You Use It</a></li>
<li><a href="#what-happens-1">What Happens</a></li>
<li><a href="#trade-offs-1">Trade-offs</a></li>
</ul>
</li>
<li><a href="#3-subagents-specialists-with-their-own-context">3. Subagents: Specialists with Their Own Context</a>
<ul>
<li><a href="#what-it-is-2">What It Is</a></li>
<li><a href="#where-it-lives-2">Where It Lives</a></li>
<li><a href="#the-dexiejs-solution-2">The Dexie.js Solution</a></li>
<li><a href="#what-happens-2">What Happens</a></li>
<li><a href="#trade-offs-2">Trade-offs</a></li>
</ul>
</li>
<li><a href="#4-skills-rich-capabilities-with-auto-discovery">4. Skills: Rich Capabilities with Auto-Discovery</a>
<ul>
<li><a href="#what-it-is-3">What It Is</a></li>
<li><a href="#where-it-lives-3">Where It Lives</a></li>
<li><a href="#how-claude-sees-skills">How Claude Sees Skills</a></li>
<li><a href="#the-dexiejs-solution-3">The Dexie.js Solution</a></li>
<li><a href="#a-minimal-does-this-even-work-skill">A Minimal “Does This Even Work?” Skill</a></li>
<li><a href="#what-happens-3">What Happens</a></li>
<li><a href="#trade-offs-3">Trade-offs</a></li>
<li><a href="#when-to-use-what">When to use what</a></li>
<li><a href="#how-they-relate">How they relate</a></li>
</ul>
</li>
<li><a href="#conclusion">Conclusion</a></li>
</ul>
<p></p></details><p></p>
<h2 id="introduction">Introduction<a class="heading-link" aria-label="Link to section" href="#introduction"><span class="heading-link-icon">#</span></a></h2>
<p>Claude Code gives you multiple ways to “teach” it project context or automate workflows, but it’s not always obvious when to use which.</p>
<p>I’ll solve the <strong>same problem four different ways</strong> so the trade-offs are concrete. Spoiler: for doc-fetching, <strong>subagents win</strong> because they keep your main context clean.</p>
<aside aria-label="New to Claude Code?" class="aside aside-tip astro-37uy2q7c"> <div class="aside-content astro-37uy2q7c"> <p class="aside-title astro-37uy2q7c"> <span class="aside-emoji astro-37uy2q7c" role="img" aria-hidden="true">💡</span> New to Claude Code? </p> <section class="aside-body astro-37uy2q7c"> <p>This post assumes familiarity with Claude Code basics. For a broader overview of all features—including MCP, hooks, and plugins—see my <span class="internal-link-wrapper astro-3tyn5ojg"> <a target="_blank" rel="noopener noreferrer" href="/posts/understanding-claude-code-full-stack/" class="internal-link astro-3tyn5ojg"> comprehensive guide to Claude Code’s feature stack </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">Understanding Claude Code&#39;s Full Stack: MCP, Skills, Subagents, and Hooks Explained</span> <span class="preview-description astro-3tyn5ojg">A practical guide to Claude Code&#39;s features — explained in the order they were introduced: MCP (2024), Claude Code core (Feb 2025), Plugins (2025), and Agent Skills (Oct 2025). What each does, how they fit together, and when to use what.</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">claude-code</span><span class="preview-tag astro-3tyn5ojg">ai</span><span class="preview-tag astro-3tyn5ojg">mcp</span> <span class="preview-tag-more astro-3tyn5ojg">+2</span> </span> <time class="preview-date astro-3tyn5ojg">Nov 9, 2025</time> </span> </span> </span>  <script>
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
</script>. If you want to automate responses to Claude Code events (like getting <span class="internal-link-wrapper astro-3tyn5ojg"> <a target="_blank" rel="noopener noreferrer" href="/posts/claude-code-notification-hooks/" class="internal-link astro-3tyn5ojg"> desktop notifications when tasks finish </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">Claude Code Notifications: Get Alerts When Tasks Finish (Hooks Setup)</span> <span class="preview-description astro-3tyn5ojg">How to set up Claude Code notifications using hooks. Get desktop alerts when Claude finishes a task, needs your input, or requests permission, instead of watching the terminal.</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">claude-code</span><span class="preview-tag astro-3tyn5ojg">notifications</span><span class="preview-tag astro-3tyn5ojg">hooks</span> <span class="preview-tag-more astro-3tyn5ojg">+1</span> </span> <time class="preview-date astro-3tyn5ojg">Nov 23, 2025</time> </span> </span> </span>  <script>
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
</script>), check out the hooks guide.</p> </section> </div> </aside> 
<hr/>
<h2 id="the-problem">The Problem<a class="heading-link" aria-label="Link to section" href="#the-problem"><span class="heading-link-icon">#</span></a></h2>
<p>Claude Code doesn’t have up-to-date training data for every library, so it can’t reliably “remember” what a docs site says today.</p>
<p><strong>The specific problem</strong>: I’m building a workout tracking app with <a href="https://dexie.org" rel="noopener noreferrer" target="_blank">Dexie.js</a> (IndexedDB wrapper). Claude keeps suggesting outdated patterns and misses things like <code>liveQuery()</code>.</p>
<p>Claude Code itself has a mechanism to fetch its own documentation. We need to do the same for our specialized libraries.</p>
<p><svg id="mermaid-0" width="100%" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" class="flowchart" style="max-width:949.09375px" viewBox="0 0 949.09375 175.96875" role="graphics-document document" aria-roledescription="flowchart-v2"><style>#mermaid-0{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;fill:#ccc;}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#mermaid-0 .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#mermaid-0 .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#mermaid-0 .error-icon{fill:#a44141;}#mermaid-0 .error-text{fill:#ddd;stroke:#ddd;}#mermaid-0 .edge-thickness-normal{stroke-width:1px;}#mermaid-0 .edge-thickness-thick{stroke-width:3.5px;}#mermaid-0 .edge-pattern-solid{stroke-dasharray:0;}#mermaid-0 .edge-thickness-invisible{stroke-width:0;fill:none;}#mermaid-0 .edge-pattern-dashed{stroke-dasharray:3;}#mermaid-0 .edge-pattern-dotted{stroke-dasharray:2;}#mermaid-0 .marker{fill:rgb(171, 75, 153);stroke:rgb(171, 75, 153);}#mermaid-0 .marker.cross{stroke:rgb(171, 75, 153);}#mermaid-0 svg{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;}#mermaid-0 p{margin:0;}#mermaid-0 .label{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;color:#ccc;}#mermaid-0 .cluster-label text{fill:#F9FFFE;}#mermaid-0 .cluster-label span{color:#F9FFFE;}#mermaid-0 .cluster-label span p{background-color:transparent;}#mermaid-0 .label text,#mermaid-0 span{fill:#ccc;color:#ccc;}#mermaid-0 .node rect,#mermaid-0 .node circle,#mermaid-0 .node ellipse,#mermaid-0 .node polygon,#mermaid-0 .node path{fill:transparent;stroke:2px;stroke-width:1px;}#mermaid-0 .rough-node .label text,#mermaid-0 .node .label text,#mermaid-0 .image-shape .label,#mermaid-0 .icon-shape .label{text-anchor:middle;}#mermaid-0 .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#mermaid-0 .rough-node .label,#mermaid-0 .node .label,#mermaid-0 .image-shape .label,#mermaid-0 .icon-shape .label{text-align:center;}#mermaid-0 .node.clickable{cursor:pointer;}#mermaid-0 .root .anchor path{fill:rgb(171, 75, 153)!important;stroke-width:0;stroke:rgb(171, 75, 153);}#mermaid-0 .arrowheadPath{fill:lightgrey;}#mermaid-0 .edgePath .path{stroke:rgb(171, 75, 153);stroke-width:2.0px;}#mermaid-0 .flowchart-link{stroke:rgb(171, 75, 153);fill:none;}#mermaid-0 .edgeLabel{background-color:hsla(0, 0%, 25%, 0);text-align:center;}#mermaid-0 .edgeLabel p{background-color:hsla(0, 0%, 25%, 0);}#mermaid-0 .edgeLabel rect{opacity:0.5;background-color:hsla(0, 0%, 25%, 0);fill:hsla(0, 0%, 25%, 0);}#mermaid-0 .labelBkg{background-color:rgba(63.75, 63.75, 63.75, 0.5);}#mermaid-0 .cluster rect{fill:transparent;stroke:rgba(255, 255, 255, 0.25);stroke-width:1px;}#mermaid-0 .cluster text{fill:#F9FFFE;}#mermaid-0 .cluster span{color:#F9FFFE;}#mermaid-0 div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:12px;background:rgb(138, 51, 123);border:1px solid rgba(255, 255, 255, 0.25);border-radius:2px;pointer-events:none;z-index:100;}#mermaid-0 .flowchartTitleText{text-anchor:middle;font-size:18px;fill:#ccc;}#mermaid-0 rect.text{fill:none;stroke-width:0;}#mermaid-0 .icon-shape,#mermaid-0 .image-shape{background-color:hsla(0, 0%, 25%, 0);text-align:center;}#mermaid-0 .icon-shape p,#mermaid-0 .image-shape p{background-color:hsla(0, 0%, 25%, 0);padding:2px;}#mermaid-0 .icon-shape rect,#mermaid-0 .image-shape rect{opacity:0.5;background-color:hsla(0, 0%, 25%, 0);fill:hsla(0, 0%, 25%, 0);}#mermaid-0 .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#mermaid-0 .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#mermaid-0 :root{--mermaid-font-family:arial,sans-serif;}</style><g><marker id="mermaid-0_flowchart-v2-pointEnd" class="marker flowchart-v2" viewBox="0 0 10 10" refX="5" refY="5" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-0_flowchart-v2-pointStart" class="marker flowchart-v2" viewBox="0 0 10 10" refX="4.5" refY="5" markerUnits="userSpaceOnUse" markerWidth="8" markerHeight="8" orient="auto"><path d="M 0 5 L 10 10 L 10 0 z" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-0_flowchart-v2-circleEnd" class="marker flowchart-v2" viewBox="0 0 10 10" refX="11" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><circle cx="5" cy="5" r="5" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></circle></marker><marker id="mermaid-0_flowchart-v2-circleStart" class="marker flowchart-v2" viewBox="0 0 10 10" refX="-1" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><circle cx="5" cy="5" r="5" class="arrowMarkerPath" style="stroke-width:1;stroke-dasharray:1, 0"></circle></marker><marker id="mermaid-0_flowchart-v2-crossEnd" class="marker cross flowchart-v2" viewBox="0 0 11 11" refX="12" refY="5.2" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M 1,1 l 9,9 M 10,1 l -9,9" class="arrowMarkerPath" style="stroke-width:2;stroke-dasharray:1, 0"></path></marker><marker id="mermaid-0_flowchart-v2-crossStart" class="marker cross flowchart-v2" viewBox="0 0 11 11" refX="-1" refY="5.2" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto"><path d="M 1,1 l 9,9 M 10,1 l -9,9" class="arrowMarkerPath" style="stroke-width:2;stroke-dasharray:1, 0"></path></marker><g class="root"><g class="clusters"></g><g class="edgePaths"><path d="M193.234,87.984L197.401,87.984C201.568,87.984,209.901,87.984,217.568,87.984C225.234,87.984,232.234,87.984,235.734,87.984L239.234,87.984" id="L_A_B_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_A_B_0" data-points="W3sieCI6MTkzLjIzNDM3NSwieSI6ODcuOTg0Mzc1fSx7IngiOjIxOC4yMzQzNzUsInkiOjg3Ljk4NDM3NX0seyJ4IjoyNDMuMjM0Mzc1LCJ5Ijo4Ny45ODQzNzV9XQ==" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M376.709,61.49L385.291,57.239C393.874,52.988,411.038,44.486,423.121,40.235C435.203,35.984,442.203,35.984,445.703,35.984L449.203,35.984" id="L_B_C_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_B_C_0" data-points="W3sieCI6Mzc2LjcwODg0ODEwMTQyMzMsInkiOjYxLjQ5MDA5ODEwMTQyMzMxNH0seyJ4Ijo0MjguMjAzMTI1LCJ5IjozNS45ODQzNzV9LHsieCI6NDUzLjIwMzEyNSwieSI6MzUuOTg0Mzc1fV0=" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M376.709,114.479L385.291,118.73C393.874,122.981,411.038,131.482,423.121,135.733C435.203,139.984,442.203,139.984,445.703,139.984L449.203,139.984" id="L_B_D_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_B_D_0" data-points="W3sieCI6Mzc2LjcwODg0ODEwMTQyMzMsInkiOjExNC40Nzg2NTE4OTg1NzY2OX0seyJ4Ijo0MjguMjAzMTI1LCJ5IjoxMzkuOTg0Mzc1fSx7IngiOjQ1My4yMDMxMjUsInkiOjEzOS45ODQzNzV9XQ==" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M686.594,139.984L690.76,139.984C694.927,139.984,703.26,139.984,710.927,139.984C718.594,139.984,725.594,139.984,729.094,139.984L732.594,139.984" id="L_D_E_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_D_E_0" data-points="W3sieCI6Njg2LjU5Mzc1LCJ5IjoxMzkuOTg0Mzc1fSx7IngiOjcxMS41OTM3NSwieSI6MTM5Ljk4NDM3NX0seyJ4Ijo3MzYuNTkzNzUsInkiOjEzOS45ODQzNzV9XQ==" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path><path d="M686.594,35.984L690.76,35.984C694.927,35.984,703.26,35.984,711.73,35.984C720.201,35.984,728.807,35.984,733.111,35.984L737.414,35.984" id="L_C_F_0" class="edge-thickness-normal edge-pattern-solid edge-thickness-normal edge-pattern-solid flowchart-link" style="" data-edge="true" data-et="edge" data-id="L_C_F_0" data-points="W3sieCI6Njg2LjU5Mzc1LCJ5IjozNS45ODQzNzV9LHsieCI6NzExLjU5Mzc1LCJ5IjozNS45ODQzNzV9LHsieCI6NzQxLjQxNDA2MjUsInkiOjM1Ljk4NDM3NX1d" marker-end="url(#mermaid-0_flowchart-v2-pointEnd)"></path></g><g class="edgeLabels"><g class="edgeLabel"><g class="label" data-id="L_A_B_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_B_C_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_B_D_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_D_E_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g><g class="edgeLabel"><g class="label" data-id="L_C_F_0" transform="translate(0, 0)"><foreignObject width="0" height="0"><div xmlns="http://www.w3.org/1999/xhtml" class="labelBkg" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="edgeLabel"></span></div></foreignObject></g></g></g><g class="nodes"><g class="node default" id="flowchart-A-0" transform="translate(100.6171875, 87.984375)"><rect class="basic label-container" style="" x="-92.6171875" y="-27" width="185.234375" height="54"></rect><g class="label" style="" transform="translate(-62.6171875, -12)"><rect></rect><foreignObject width="125.234375" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>User Question</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-B-1" transform="translate(323.21875, 87.984375)"><polygon points="79.984375,0 159.96875,-79.984375 79.984375,-159.96875 0,-79.984375" class="label-container" transform="translate(-79.484375, 79.984375)"></polygon><g class="label" style="" transform="translate(-52.984375, -12)"><rect></rect><foreignObject width="105.96875" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Claude Code</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-C-3" transform="translate(569.8984375, 35.984375)"><rect class="basic label-container" style="" x="-116.6953125" y="-27" width="233.390625" height="54"></rect><g class="label" style="" transform="translate(-86.6953125, -12)"><rect></rect><foreignObject width="173.390625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Outdated Knowledge</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-D-5" transform="translate(569.8984375, 139.984375)"><rect class="basic label-container" style="" x="-116.6953125" y="-27" width="233.390625" height="54"></rect><g class="label" style="" transform="translate(-86.6953125, -12)"><rect></rect><foreignObject width="173.390625" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Fetch Current Docs</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-E-7" transform="translate(838.84375, 139.984375)"><rect class="basic label-container" style="" x="-102.25" y="-27" width="204.5" height="54"></rect><g class="label" style="" transform="translate(-72.25, -12)"><rect></rect><foreignObject width="144.5" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Accurate Answer</p></span></div></foreignObject></g></g><g class="node default" id="flowchart-F-9" transform="translate(838.84375, 35.984375)"><rect class="basic label-container" style="" x="-97.4296875" y="-27" width="194.859375" height="54"></rect><g class="label" style="" transform="translate(-67.4296875, -12)"><rect></rect><foreignObject width="134.859375" height="24"><div xmlns="http://www.w3.org/1999/xhtml" style="display:table-cell;white-space:nowrap;line-height:1.5;max-width:200px;text-align:center"><span class="nodeLabel"><p>Wrong Patterns</p></span></div></foreignObject></g></g></g></g></g></svg></p>
<p>Let’s solve it with all four tools, then compare.</p>
<hr/>
<h2 id="1-claudemd-always-on-project-memory">1. CLAUDE.md: Always-On Project Memory<a class="heading-link" aria-label="Link to section" href="#1-claudemd-always-on-project-memory"><span class="heading-link-icon">#</span></a></h2>
<h3 id="what-it-is">What It Is<a class="heading-link" aria-label="Link to section" href="#what-it-is"><span class="heading-link-icon">#</span></a></h3>
<p>A markdown file that’s <strong>automatically loaded</strong> every time you start Claude Code. Think of it as your project’s “memory card.”</p>
<blockquote>
<p><strong>CLAUDE.md</strong>: Persistent project instructions that Claude reads at the start of every conversation.</p>
</blockquote>
<h3 id="where-it-lives">Where It Lives<a class="heading-link" aria-label="Link to section" href="#where-it-lives"><span class="heading-link-icon">#</span></a></h3>
<nav class="file-tree astro-htwbjus4" aria-label="File tree"> <ul class="file-tree__list astro-htwbjus4"> <li class="file-tree__item astro-o25vlg2d" style="--level: 0;"> <details class="file-tree__folder astro-o25vlg2d" open> <summary class="astro-o25vlg2d"> <span class="file-tree__caret astro-o25vlg2d" aria-hidden="true">
▸
</span> <svg class="file-tree__icon astro-o25vlg2d" aria-hidden="true" viewBox="0 0 16 16"> <path fill="currentColor" d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z" class="astro-o25vlg2d"></path> </svg> <span class="file-tree__name astro-o25vlg2d">project-root</span>  </summary> <ul class="file-tree__list astro-o25vlg2d"> <li class="file-tree__item astro-o25vlg2d" style="--level: 1;">   <span class="file-tree__file astro-o25vlg2d">  <svg class="file-tree__icon file-tree__icon--file file-tree__icon--colored astro-o25vlg2d" aria-hidden="true" viewBox="0 0 24 24"> <path fill="#519ABA" d="M22.27 19.385H1.73A1.73 1.73 0 010 17.655V6.345a1.73 1.73 0 011.73-1.73h20.54A1.73 1.73 0 0124 6.345v11.308a1.73 1.73 0 01-1.73 1.731zM5.769 15.923v-4.5l2.308 2.885 2.307-2.885v4.5h2.308V8.078h-2.308l-2.307 2.885-2.308-2.885H3.46v7.847zM21.232 12h-2.309V8.077h-2.307V12h-2.308l3.461 4.039z" class="astro-o25vlg2d"></path> </svg>  <span class="file-tree__name astro-o25vlg2d">CLAUDE.md</span> <span class="file-tree__comment astro-o25vlg2d">// Project-level</span> </span> </li> <li class="file-tree__item astro-o25vlg2d" style="--level: 1;"> <details class="file-tree__folder astro-o25vlg2d"> <summary class="astro-o25vlg2d"> <span class="file-tree__caret astro-o25vlg2d" aria-hidden="true">
▸
</span> <svg class="file-tree__icon astro-o25vlg2d" aria-hidden="true" viewBox="0 0 16 16"> <path fill="currentColor" d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z" class="astro-o25vlg2d"></path> </svg> <span class="file-tree__name astro-o25vlg2d">.claude</span>  </summary> <ul class="file-tree__list astro-o25vlg2d"> <li class="file-tree__item astro-o25vlg2d" style="--level: 2;">   <span class="file-tree__file astro-o25vlg2d">  <svg class="file-tree__icon file-tree__icon--file file-tree__icon--colored astro-o25vlg2d" aria-hidden="true" viewBox="0 0 24 24"> <path fill="#519ABA" d="M22.27 19.385H1.73A1.73 1.73 0 010 17.655V6.345a1.73 1.73 0 011.73-1.73h20.54A1.73 1.73 0 0124 6.345v11.308a1.73 1.73 0 01-1.73 1.731zM5.769 15.923v-4.5l2.308 2.885 2.307-2.885v4.5h2.308V8.078h-2.308l-2.307 2.885-2.308-2.885H3.46v7.847zM21.232 12h-2.309V8.077h-2.307V12h-2.308l3.461 4.039z" class="astro-o25vlg2d"></path> </svg>  <span class="file-tree__name astro-o25vlg2d">CLAUDE.md</span> <span class="file-tree__comment astro-o25vlg2d">// Alternative location</span> </span> </li>  </ul> </details>   </li> <li class="file-tree__item astro-o25vlg2d" style="--level: 1;"> <details class="file-tree__folder astro-o25vlg2d"> <summary class="astro-o25vlg2d"> <span class="file-tree__caret astro-o25vlg2d" aria-hidden="true">
▸
</span> <svg class="file-tree__icon astro-o25vlg2d" aria-hidden="true" viewBox="0 0 16 16"> <path fill="currentColor" d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z" class="astro-o25vlg2d"></path> </svg> <span class="file-tree__name astro-o25vlg2d">tests</span>  </summary> <ul class="file-tree__list astro-o25vlg2d"> <li class="file-tree__item astro-o25vlg2d" style="--level: 2;">   <span class="file-tree__file astro-o25vlg2d">  <svg class="file-tree__icon file-tree__icon--file file-tree__icon--colored astro-o25vlg2d" aria-hidden="true" viewBox="0 0 24 24"> <path fill="#519ABA" d="M22.27 19.385H1.73A1.73 1.73 0 010 17.655V6.345a1.73 1.73 0 011.73-1.73h20.54A1.73 1.73 0 0124 6.345v11.308a1.73 1.73 0 01-1.73 1.731zM5.769 15.923v-4.5l2.308 2.885 2.307-2.885v4.5h2.308V8.078h-2.308l-2.307 2.885-2.308-2.885H3.46v7.847zM21.232 12h-2.309V8.077h-2.307V12h-2.308l3.461 4.039z" class="astro-o25vlg2d"></path> </svg>  <span class="file-tree__name astro-o25vlg2d">CLAUDE.md</span> <span class="file-tree__comment astro-o25vlg2d">// Loaded when reading test files</span> </span> </li>  </ul> </details>   </li>  </ul> </details>   </li>  </ul> </nav> 
<h3 id="nested-claudemd-files">Nested CLAUDE.md Files<a class="heading-link" aria-label="Link to section" href="#nested-claudemd-files"><span class="heading-link-icon">#</span></a></h3>
<p>Claude Code also discovers <strong>nested CLAUDE.md files</strong> in subdirectories. When Claude reads files from a directory containing its own <code>CLAUDE.md</code>, that file gets added to the context automatically.</p>
<p>This is useful for directory-specific instructions:</p>
<ul>
<li><code>tests/CLAUDE.md</code> — testing conventions, preferred mocking patterns</li>
<li><code>src/db/CLAUDE.md</code> — database-specific patterns and constraints</li>
<li><code>src/components/CLAUDE.md</code> — component architecture guidelines</li>
</ul>
<p>The nested file is only loaded when Claude actually accesses files in that directory, keeping your main context lean until you need that specialized knowledge.</p>
<h3 id="the-dexiejs-solution">The Dexie.js Solution<a class="heading-link" aria-label="Link to section" href="#the-dexiejs-solution"><span class="heading-link-icon">#</span></a></h3>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="markdown"><code><span class="line"><span style="color:#89DDFF;font-weight:bold">#</span><span style="color:#89DDFF;font-weight:bold"> CLAUDE.md</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Database</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">We use Dexie.js for IndexedDB. Before implementing any database code:</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">1.</span><span style="color:#9AA5CE"> Fetch the docs index from https://dexie.org/llms.txt</span></span>
<span class="line"><span style="color:#89DDFF">2.</span><span style="color:#9AA5CE"> Use </span><span style="color:#89DDFF">`liveQuery()`</span><span style="color:#9AA5CE"> for reactive data binding</span></span>
<span class="line"><span style="color:#89DDFF">3.</span><span style="color:#9AA5CE"> Follow the repository pattern in </span><span style="color:#89DDFF">`src/db/`</span></span>
<span class="line"><span style="color:#89DDFF">4.</span><span style="color:#9AA5CE"> Always handle </span><span style="color:#89DDFF">`ConstraintError`</span><span style="color:#9AA5CE"> for duplicate keys</span></span></code><button type="button" class="copy" data-code="# CLAUDE.md

## Database

We use Dexie.js for IndexedDB. Before implementing any database code:

1. Fetch the docs index from https://dexie.org/llms.txt
2. Use `liveQuery()` for reactive data binding
3. Follow the repository pattern in `src/db/`
4. Always handle `ConstraintError` for duplicate keys" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h3 id="what-happens">What Happens<a class="heading-link" aria-label="Link to section" href="#what-happens"><span class="heading-link-icon">#</span></a></h3>
<p>Every conversation starts with Claude knowing “fetch Dexie docs before writing database code.”</p>
<p>The catch is <strong>context drift</strong>: in long sessions, the model can gradually deprioritize earlier system-level instructions in favor of the most recent conversation history.</p>
<h3 id="trade-offs">Trade-offs<a class="heading-link" aria-label="Link to section" href="#trade-offs"><span class="heading-link-icon">#</span></a></h3>





















<table><thead><tr><th>✅ Pros</th><th>❌ Cons</th></tr></thead><tbody><tr><td data-label="✅ Pros">Zero effort—always loaded</td><td data-label="❌ Cons"><strong>Context Drift</strong>: Claude forgets instructions as sessions get longer</td></tr><tr><td data-label="✅ Pros">Team-shared via git</td><td data-label="❌ Cons">No dedicated context window—competes with your conversation</td></tr><tr><td data-label="✅ Pros">Simple to maintain</td><td data-label="❌ Cons">No enforcement—Claude decides whether to follow</td></tr></tbody></table>
<hr/>
<h2 id="2-slash-commands-simple-skills-you-invoke">2. Slash Commands: Simple Skills You Invoke<a class="heading-link" aria-label="Link to section" href="#2-slash-commands-simple-skills-you-invoke"><span class="heading-link-icon">#</span></a></h2>
<h3 id="what-it-is-1">What It Is<a class="heading-link" aria-label="Link to section" href="#what-it-is-1"><span class="heading-link-icon">#</span></a></h3>
<p>A saved prompt you invoke by typing <code>/command-name</code>. Like a macro or keyboard shortcut for prompts.</p>
<p>Slash commands can be invoked explicitly (you type <code>/command</code>) and can also be auto-invoked by Claude when the command’s <code>description</code> matches the task.</p>
<p>Slash commands can also <strong>orchestrate other behavior</strong>: you can spell out in the command itself that it should spin up a subagent (or a specific subagent), call out a particular skill/workflow, and generally “pipeline” the work (e.g., research → codebase scan → write a doc) instead of trying to do everything in one shot.</p>
<p>The main difference vs skills is <strong>packaging + UX</strong>: slash commands are single-file entries with great terminal <code>/...</code> discovery/autocomplete; skills are usually directories with supporting files (patterns, templates, scripts).</p>
<aside aria-label="Deep dive" class="aside aside-info astro-37uy2q7c"> <div class="aside-content astro-37uy2q7c"> <p class="aside-title astro-37uy2q7c"> <span class="aside-emoji astro-37uy2q7c" role="img" aria-hidden="true">ℹ️</span> Deep dive </p> <section class="aside-body astro-37uy2q7c"> <p>Want a full walkthrough? See my <span class="internal-link-wrapper astro-3tyn5ojg"> <a target="_blank" rel="noopener noreferrer" href="/posts/claude-code-slash-commands-guide/" class="internal-link astro-3tyn5ojg"> slash commands guide </a> <span class="preview-card astro-3tyn5ojg" role="tooltip"> <span class="preview-content astro-3tyn5ojg"> <span class="preview-title astro-3tyn5ojg">How to Speed Up Your Claude Code Experience with Slash Commands</span> <span class="preview-description astro-3tyn5ojg">Learn how to transform Claude Code from a chatbot into a deterministic engine using Slash Commands. This guide covers the technical setup and a complete &#39;Full Circle&#39; workflow that automates your entire feature lifecycle.</span> <span class="preview-tags astro-3tyn5ojg"> <span class="preview-tag astro-3tyn5ojg">ai</span><span class="preview-tag astro-3tyn5ojg">claude-code</span>  </span> <time class="preview-date astro-3tyn5ojg">Nov 22, 2025</time> </span> </span> </span>  <script>
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
<h3 id="where-it-lives-1">Where It Lives<a class="heading-link" aria-label="Link to section" href="#where-it-lives-1"><span class="heading-link-icon">#</span></a></h3>
<nav class="file-tree astro-htwbjus4" aria-label="File tree"> <ul class="file-tree__list astro-htwbjus4"> <li class="file-tree__item astro-o25vlg2d" style="--level: 0;"> <details class="file-tree__folder astro-o25vlg2d" open> <summary class="astro-o25vlg2d"> <span class="file-tree__caret astro-o25vlg2d" aria-hidden="true">
▸
</span> <svg class="file-tree__icon astro-o25vlg2d" aria-hidden="true" viewBox="0 0 16 16"> <path fill="currentColor" d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z" class="astro-o25vlg2d"></path> </svg> <span class="file-tree__name astro-o25vlg2d">.claude</span>  </summary> <ul class="file-tree__list astro-o25vlg2d"> <li class="file-tree__item astro-o25vlg2d" style="--level: 1;"> <details class="file-tree__folder astro-o25vlg2d" open> <summary class="astro-o25vlg2d"> <span class="file-tree__caret astro-o25vlg2d" aria-hidden="true">
▸
</span> <svg class="file-tree__icon astro-o25vlg2d" aria-hidden="true" viewBox="0 0 16 16"> <path fill="currentColor" d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z" class="astro-o25vlg2d"></path> </svg> <span class="file-tree__name astro-o25vlg2d">commands</span>  </summary> <ul class="file-tree__list astro-o25vlg2d"> <li class="file-tree__item astro-o25vlg2d" style="--level: 2;">   <span class="file-tree__file astro-o25vlg2d">  <svg class="file-tree__icon file-tree__icon--file file-tree__icon--colored astro-o25vlg2d" aria-hidden="true" viewBox="0 0 24 24"> <path fill="#519ABA" d="M22.27 19.385H1.73A1.73 1.73 0 010 17.655V6.345a1.73 1.73 0 011.73-1.73h20.54A1.73 1.73 0 0124 6.345v11.308a1.73 1.73 0 01-1.73 1.731zM5.769 15.923v-4.5l2.308 2.885 2.307-2.885v4.5h2.308V8.078h-2.308l-2.307 2.885-2.308-2.885H3.46v7.847zM21.232 12h-2.309V8.077h-2.307V12h-2.308l3.461 4.039z" class="astro-o25vlg2d"></path> </svg>  <span class="file-tree__name astro-o25vlg2d">dexie-help.md</span>  </span> </li>  </ul> </details>   </li>  </ul> </details>   </li>  </ul> </nav> 
<h3 id="the-dexiejs-solution-1">The Dexie.js Solution<a class="heading-link" aria-label="Link to section" href="#the-dexiejs-solution-1"><span class="heading-link-icon">#</span></a></h3>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="markdown"><code><span class="line"><span style="color:#89DDFF">---</span></span>
<span class="line"><span style="color:#F7768E">description</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> Get Dexie.js guidance with current documentation</span></span>
<span class="line"><span style="color:#F7768E">allowed-tools</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> Read, Grep, Glob, WebFetch</span></span>
<span class="line"><span style="color:#89DDFF">---</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">First, fetch the documentation index from https://dexie.org/llms.txt</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">Then, based on the user&#39;s question, fetch the relevant documentation pages.</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">Finally, answer the following question using the current documentation:</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">$ARGUMENTS</span></span></code><button type="button" class="copy" data-code="---
description: Get Dexie.js guidance with current documentation
allowed-tools: Read, Grep, Glob, WebFetch
---

First, fetch the documentation index from https://dexie.org/llms.txt

Then, based on the user's question, fetch the relevant documentation pages.

Finally, answer the following question using the current documentation:

$ARGUMENTS" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h3 id="manual-orchestration-example-research">Manual Orchestration Example (Research)<a class="heading-link" aria-label="Link to section" href="#manual-orchestration-example-research"><span class="heading-link-icon">#</span></a></h3>
<p>If you want a slash command that <strong>explicitly launches multiple subagents in parallel</strong> and then produces an artifact (like a research note in <code>docs/research/</code>), you can encode that directly in the command definition.</p>
<details class="collapsible astro-kncz7yy6"> <summary class="collapsible-summary astro-kncz7yy6"> <span class="collapsible-icon astro-kncz7yy6"> <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="astro-kncz7yy6"> <polyline points="9 18 15 12 9 6" class="astro-kncz7yy6"></polyline> </svg> </span> research.md (custom command) </summary> <div class="collapsible-content astro-kncz7yy6"> <pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="markdown"><code><span class="line"><span style="color:#89DDFF">---</span></span>
<span class="line"><span style="color:#F7768E">description</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> Research a problem using web search, documentation, and codebase exploration</span></span>
<span class="line"><span style="color:#F7768E">allowed-tools</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> Task, WebSearch, WebFetch, Grep, Glob, Read, Write, Bash</span></span>
<span class="line"><span style="color:#89DDFF">---</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF;font-weight:bold">#</span><span style="color:#89DDFF;font-weight:bold"> Research: $ARGUMENTS</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">Research the following problem or question:</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF;font-style:italic">&gt;</span><span style="color:#C0CAF5;font-weight:bold"> **$ARGUMENTS**</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Instructions</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">Conduct thorough research like a senior developer. Launch multiple subagents in parallel to gather information from different sources.</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7;font-weight:bold">###</span><span style="color:#7AA2F7;font-weight:bold"> Step 1: Launch Parallel Research Agents</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">Use the Task tool to spawn these subagents </span><span style="color:#C0CAF5;font-weight:bold">**in parallel**</span><span style="color:#9AA5CE"> (all in a single message):</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">1.</span><span style="color:#C0CAF5;font-weight:bold"> **Web Documentation Agent**</span><span style="color:#9AA5CE"> (subagent_type: general-purpose)</span></span>
<span class="line"><span style="color:#89DDFF">  -</span><span style="color:#9AA5CE"> Search official documentation for the topic</span></span>
<span class="line"><span style="color:#89DDFF">  -</span><span style="color:#9AA5CE"> Find best practices and recommended patterns</span></span>
<span class="line"><span style="color:#89DDFF">  -</span><span style="color:#9AA5CE"> Locate relevant GitHub issues or discussions</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">2.</span><span style="color:#C0CAF5;font-weight:bold"> **Stack Overflow Agent**</span><span style="color:#9AA5CE"> (subagent_type: general-purpose)</span></span>
<span class="line"><span style="color:#89DDFF">  -</span><span style="color:#9AA5CE"> Search Stack Overflow for similar problems and solutions</span></span>
<span class="line"><span style="color:#89DDFF">  -</span><span style="color:#9AA5CE"> Find highly-voted and accepted answers</span></span>
<span class="line"><span style="color:#89DDFF">  -</span><span style="color:#9AA5CE"> Note common pitfalls and gotchas</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">3.</span><span style="color:#C0CAF5;font-weight:bold"> **Codebase Explorer Agent**</span><span style="color:#9AA5CE"> (subagent_type: Explore)</span></span>
<span class="line"><span style="color:#89DDFF">  -</span><span style="color:#9AA5CE"> Search the codebase for related patterns</span></span>
<span class="line"><span style="color:#89DDFF">  -</span><span style="color:#9AA5CE"> Find existing solutions to similar problems</span></span>
<span class="line"><span style="color:#89DDFF">  -</span><span style="color:#9AA5CE"> Identify relevant files, functions, or components</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7;font-weight:bold">###</span><span style="color:#7AA2F7;font-weight:bold"> Step 2: Create Research Document</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">After all agents complete, create a markdown file at </span><span style="color:#89DDFF">`docs/research/&lt;topic-slug&gt;.md`</span><span style="color:#9AA5CE">.</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">Generate the filename from the research topic:</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Convert to lowercase</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Replace spaces with hyphens</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Remove special characters</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Add today&#39;s date as prefix: </span><span style="color:#89DDFF">`YYYY-MM-DD-&lt;topic-slug&gt;.md`</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">Example: &quot;Vue 3 Suspense&quot; → </span><span style="color:#89DDFF">`docs/research/2024-12-06-vue-3-suspense.md`</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">First, create the research folder if it doesn&#39;t exist:</span></span>
<span class="line"><span style="color:#89DDFF">```bash</span></span>
<span class="line"><span style="color:#C0CAF5">mkdir </span><span style="color:#E0AF68">-p</span><span style="color:#9ECE6A"> docs/research</span></span>
<span class="line"><span style="color:#89DDFF">```</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7;font-weight:bold">###</span><span style="color:#7AA2F7;font-weight:bold"> Step 3: Write the Research Document</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">Structure the document with these sections:</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">```markdown</span></span>
<span class="line"><span style="color:#89DDFF;font-weight:bold">#</span><span style="color:#89DDFF;font-weight:bold"> Research: </span><span style="color:#BA3C97;font-weight:bold">&lt;</span><span style="color:#DE5971;font-weight:bold">Topic</span><span style="color:#BA3C97;font-weight:bold">&gt;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5;font-weight:bold">**Date:**</span><span style="color:#BA3C97"> &lt;</span><span style="color:#DE5971">YYYY-MM-DD</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#C0CAF5;font-weight:bold">**Status:**</span><span style="color:#C0CAF5"> Complete</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Problem Statement</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#DE5971">Describe </span><span style="color:#BB9AF7">the</span><span style="color:#BB9AF7"> problem</span><span style="color:#BB9AF7"> and</span><span style="color:#BB9AF7"> why</span><span style="color:#BB9AF7"> it</span><span style="color:#BB9AF7"> matters</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5">## Key Findings</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#DE5971">Summarize </span><span style="color:#BB9AF7">the</span><span style="color:#BB9AF7"> most</span><span style="color:#BB9AF7"> relevant</span><span style="color:#BB9AF7"> solutions</span><span style="color:#BB9AF7"> and</span><span style="color:#BB9AF7"> approaches</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5">## Codebase Patterns</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#DE5971">Document </span><span style="color:#BB9AF7">how</span><span style="color:#BB9AF7"> the</span><span style="color:#BB9AF7"> current</span><span style="color:#BB9AF7"> codebase</span><span style="color:#BB9AF7"> handles</span><span style="color:#BB9AF7"> similar</span><span style="color:#BB9AF7"> cases</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5">## Recommended Approach</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#DE5971">Provide </span><span style="color:#BB9AF7">your</span><span style="color:#BB9AF7"> recommendation</span><span style="color:#BB9AF7"> based</span><span style="color:#BB9AF7"> on</span><span style="color:#BB9AF7"> all</span><span style="color:#BB9AF7"> research</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5">## Sources</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5">- [Source Title](URL) - Brief description</span></span>
<span class="line"><span style="color:#C0CAF5">- [Source Title](URL) - Brief description</span></span>
<span class="line"><span style="color:#89DDFF">```</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7;font-weight:bold">###</span><span style="color:#7AA2F7;font-weight:bold"> Guidelines</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Prioritize official documentation over blog posts</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Prefer solutions that match existing codebase patterns</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Note version-specific considerations (Vue 3, TypeScript, etc.)</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Flag conflicting information across sources</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Write concise, actionable content</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Use active voice throughout the document</span></span>
<span class="line"></span>
<span class="line"><span style="color:#7AA2F7;font-weight:bold">###</span><span style="color:#7AA2F7;font-weight:bold"> Step 4: Confirm Completion</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">After writing the file, output the file path so the user can find it later.</span></span></code><button type="button" class="copy" data-code="---
description: Research a problem using web search, documentation, and codebase exploration
allowed-tools: Task, WebSearch, WebFetch, Grep, Glob, Read, Write, Bash
---

# Research: $ARGUMENTS

Research the following problem or question:

> **$ARGUMENTS**

## Instructions

Conduct thorough research like a senior developer. Launch multiple subagents in parallel to gather information from different sources.

### Step 1: Launch Parallel Research Agents

Use the Task tool to spawn these subagents **in parallel** (all in a single message):

1. **Web Documentation Agent** (subagent_type: general-purpose)
  - Search official documentation for the topic
  - Find best practices and recommended patterns
  - Locate relevant GitHub issues or discussions

2. **Stack Overflow Agent** (subagent_type: general-purpose)
  - Search Stack Overflow for similar problems and solutions
  - Find highly-voted and accepted answers
  - Note common pitfalls and gotchas

3. **Codebase Explorer Agent** (subagent_type: Explore)
  - Search the codebase for related patterns
  - Find existing solutions to similar problems
  - Identify relevant files, functions, or components

### Step 2: Create Research Document

After all agents complete, create a markdown file at `docs/research/<topic-slug>.md`.

Generate the filename from the research topic:
- Convert to lowercase
- Replace spaces with hyphens
- Remove special characters
- Add today's date as prefix: `YYYY-MM-DD-<topic-slug>.md`

Example: &#34;Vue 3 Suspense&#34; → `docs/research/2024-12-06-vue-3-suspense.md`

First, create the research folder if it doesn't exist:
```bash
mkdir -p docs/research
```

### Step 3: Write the Research Document

Structure the document with these sections:

```markdown
# Research: <Topic>

**Date:** <YYYY-MM-DD>
**Status:** Complete

## Problem Statement

<Describe the problem and why it matters>

## Key Findings

<Summarize the most relevant solutions and approaches>

## Codebase Patterns

<Document how the current codebase handles similar cases>

## Recommended Approach

<Provide your recommendation based on all research>

## Sources

- [Source Title](URL) - Brief description
- [Source Title](URL) - Brief description
```

### Guidelines

- Prioritize official documentation over blog posts
- Prefer solutions that match existing codebase patterns
- Note version-specific considerations (Vue 3, TypeScript, etc.)
- Flag conflicting information across sources
- Write concise, actionable content
- Use active voice throughout the document

### Step 4: Confirm Completion

After writing the file, output the file path so the user can find it later." onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre> </div> </details>  
<h3 id="how-you-use-it">How You Use It<a class="heading-link" aria-label="Link to section" href="#how-you-use-it"><span class="heading-link-icon">#</span></a></h3>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="bash"><code><span class="line"><span style="color:#C0CAF5">/dexie-help</span><span style="color:#9ECE6A"> how</span><span style="color:#9ECE6A"> do</span><span style="color:#9ECE6A"> I</span><span style="color:#9ECE6A"> create</span><span style="color:#9ECE6A"> a</span><span style="color:#9ECE6A"> compound</span><span style="color:#9ECE6A"> index?</span></span></code><button type="button" class="copy" data-code="/dexie-help how do I create a compound index?" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h3 id="what-happens-1">What Happens<a class="heading-link" aria-label="Link to section" href="#what-happens-1"><span class="heading-link-icon">#</span></a></h3>
<p>Claude fetches the docs, finds the relevant pages, and answers your question—triggered explicitly.</p>
<h3 id="trade-offs-1">Trade-offs<a class="heading-link" aria-label="Link to section" href="#trade-offs-1"><span class="heading-link-icon">#</span></a></h3>





















<table><thead><tr><th>✅ Pros</th><th>❌ Cons</th></tr></thead><tbody><tr><td data-label="✅ Pros">You control exactly when it runs</td><td data-label="❌ Cons">Must remember to type <code>/dexie-help</code></td></tr><tr><td data-label="✅ Pros">Can pass arguments for specific questions</td><td data-label="❌ Cons">One-shot—doesn’t persist knowledge across messages</td></tr><tr><td data-label="✅ Pros">Simple single-file setup</td><td data-label="❌ Cons">Auto-triggering depends on <code>description</code> match</td></tr></tbody></table>
<hr/>
<h2 id="3-subagents-specialists-with-their-own-context">3. Subagents: Specialists with Their Own Context<a class="heading-link" aria-label="Link to section" href="#3-subagents-specialists-with-their-own-context"><span class="heading-link-icon">#</span></a></h2>
<h3 id="what-it-is-2">What It Is<a class="heading-link" aria-label="Link to section" href="#what-it-is-2"><span class="heading-link-icon">#</span></a></h3>
<p>A specialized AI “persona” with its own context window. Claude <strong>delegates entire tasks</strong> to it and gets results back.</p>
<p>Because fetching the Dexie docs involves reading multiple pages and creates a lot of context noise, keeping this inside a subagent prevents your main chat from hitting context limits.</p>
<blockquote>
<p><strong>Subagent</strong>: An isolated Claude instance that works on a task independently and returns only the results to your main conversation.</p>
</blockquote>
<div class="alert alert-tip astro-7kdbuayl"> <p class="alert-title astro-7kdbuayl"> <span class="alert-icon astro-7kdbuayl">💪</span> Subagents keep your main context clean </p> <div class="alert-content astro-7kdbuayl"> <p>Even when the task is “just exploration,” subagents are a great default because they let Claude do <strong>lots of reading/searching</strong> without dumping everything into your main thread.</p><p>This is especially useful in <strong>plan mode</strong>: Claude Code will typically kick off an <code>Explore</code>-style subagent to scan the repo and return a distilled map of relevant files/patterns, so your main conversation stays focused and doesn’t blow up.</p> </div> </div> 
<p>Claude Code also supports <strong>async agents</strong>: fire one off, let it cook while you keep working, then it comes back with its updates when it’s done. If you launch an agent and want to keep typing in your main session, you can send it to the background with <code>Ctrl + B</code>.</p>
<div class="alert alert-info astro-7kdbuayl"> <p class="alert-title astro-7kdbuayl"> <span class="alert-icon astro-7kdbuayl"></span> Claude Code does this too </p> <div class="alert-content astro-7kdbuayl"> <p>Claude Code’s own system prompt includes a built-in “documentation lookup” workflow that uses a subagent:</p><blockquote>
<p>-&gt; Looking up your own documentation:
When the user directly asks about any of the following:</p>
<ul>
<li>how to use Claude Code (eg. “can Claude Code do…”, “does Claude Code have…”)</li>
<li>what you’re able to do as Claude Code in second person (eg. “are you able…”, “can you do…”)</li>
<li>about how they might do something with Claude Code (eg. “how do I…”, “how can I…”)</li>
<li>how to use a specific Claude Code feature (eg. implement a hook, write a skill, or install an MCP server)</li>
<li>how to use the Claude Agent SDK, or asks you to write code that uses the Claude Agent SDK</li>
</ul>
<p>Use the Task tool with subagent_type=‘claude-code-guide’ to get accurate information from the official Claude Code and Claude Agent SDK documentation.</p>
</blockquote><p>Source: <a href="https://github.com/marckrenn/cc-mvp-prompts/blob/main/cc-prompt.md" rel="noopener noreferrer" target="_blank">https://github.com/marckrenn/cc-mvp-prompts/blob/main/cc-prompt.md</a></p> </div> </div> 
<h3 id="where-it-lives-2">Where It Lives<a class="heading-link" aria-label="Link to section" href="#where-it-lives-2"><span class="heading-link-icon">#</span></a></h3>
<nav class="file-tree astro-htwbjus4" aria-label="File tree"> <ul class="file-tree__list astro-htwbjus4"> <li class="file-tree__item astro-o25vlg2d" style="--level: 0;"> <details class="file-tree__folder astro-o25vlg2d" open> <summary class="astro-o25vlg2d"> <span class="file-tree__caret astro-o25vlg2d" aria-hidden="true">
▸
</span> <svg class="file-tree__icon astro-o25vlg2d" aria-hidden="true" viewBox="0 0 16 16"> <path fill="currentColor" d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z" class="astro-o25vlg2d"></path> </svg> <span class="file-tree__name astro-o25vlg2d">.claude</span>  </summary> <ul class="file-tree__list astro-o25vlg2d"> <li class="file-tree__item astro-o25vlg2d" style="--level: 1;"> <details class="file-tree__folder astro-o25vlg2d" open> <summary class="astro-o25vlg2d"> <span class="file-tree__caret astro-o25vlg2d" aria-hidden="true">
▸
</span> <svg class="file-tree__icon astro-o25vlg2d" aria-hidden="true" viewBox="0 0 16 16"> <path fill="currentColor" d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z" class="astro-o25vlg2d"></path> </svg> <span class="file-tree__name astro-o25vlg2d">agents</span>  </summary> <ul class="file-tree__list astro-o25vlg2d"> <li class="file-tree__item astro-o25vlg2d" style="--level: 2;">   <span class="file-tree__file astro-o25vlg2d">  <svg class="file-tree__icon file-tree__icon--file file-tree__icon--colored astro-o25vlg2d" aria-hidden="true" viewBox="0 0 24 24"> <path fill="#519ABA" d="M22.27 19.385H1.73A1.73 1.73 0 010 17.655V6.345a1.73 1.73 0 011.73-1.73h20.54A1.73 1.73 0 0124 6.345v11.308a1.73 1.73 0 01-1.73 1.731zM5.769 15.923v-4.5l2.308 2.885 2.307-2.885v4.5h2.308V8.078h-2.308l-2.307 2.885-2.308-2.885H3.46v7.847zM21.232 12h-2.309V8.077h-2.307V12h-2.308l3.461 4.039z" class="astro-o25vlg2d"></path> </svg>  <span class="file-tree__name astro-o25vlg2d">dexie-specialist.md</span>  </span> </li>  </ul> </details>   </li>  </ul> </details>   </li>  </ul> </nav> 
<h3 id="the-dexiejs-solution-2">The Dexie.js Solution<a class="heading-link" aria-label="Link to section" href="#the-dexiejs-solution-2"><span class="heading-link-icon">#</span></a></h3>
<details class="collapsible astro-kncz7yy6"> <summary class="collapsible-summary astro-kncz7yy6"> <span class="collapsible-icon astro-kncz7yy6"> <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="astro-kncz7yy6"> <polyline points="9 18 15 12 9 6" class="astro-kncz7yy6"></polyline> </svg> </span> dexie-specialist.md (full definition) </summary> <div class="collapsible-content astro-kncz7yy6"> <pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="markdown"><code><span class="line"><span style="color:#89DDFF">---</span></span>
<span class="line"><span style="color:#F7768E">name</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> dexie-db-specialist</span></span>
<span class="line"><span style="color:#F7768E">description</span><span style="color:#89DDFF">:</span><span style="color:#F7768E"> Use this agent when the task involves Dexie.js or IndexedDB in any way - implementing, modifying, querying, reviewing, or improving database code. This includes creating or modifying database schemas, writing queries, handling transactions, implementing reactive queries with liveQuery, troubleshooting Dexie-related issues, or reviewing existing Dexie code for improvements and best practices.\n\nExamples:\n\n&lt;example&gt;\nContext</span><span style="color:#89DDFF">:</span><span style="color:#F7768E"> User asks about improving their Dexie.js code.\nuser</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">What can I improve on this codebase when it comes to Dexie?</span><span style="color:#89DDFF">&quot;</span><span style="color:#F7768E">\nassistant</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">I&#39;ll use the dexie-db-specialist agent to review your Dexie.js implementation against current best practices.</span><span style="color:#89DDFF">&quot;</span><span style="color:#F7768E">\n&lt;commentary&gt;\nSince the user is asking about Dexie.js improvements, use the dexie-db-specialist agent to fetch the latest documentation and review the existing code for optimization opportunities, missing features, and best practice violations.\n&lt;/commentary&gt;\n&lt;/example&gt;\n\n&lt;example&gt;\nContext</span><span style="color:#89DDFF">:</span><span style="color:#F7768E"> User needs to add a new table to the database.\nuser</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">I need to add a new &#39;goals&#39; table to track workout goals</span><span style="color:#89DDFF">&quot;</span><span style="color:#F7768E">\nassistant</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">I&#39;ll use the dexie-db-specialist agent to implement this correctly.</span><span style="color:#89DDFF">&quot;</span><span style="color:#F7768E">\n&lt;commentary&gt;\nSince the user needs to modify the Dexie database schema, use the dexie-db-specialist agent to first fetch the latest Dexie.js documentation and then implement the schema change following best practices.\n&lt;/commentary&gt;\n&lt;/example&gt;\n\n&lt;example&gt;\nContext</span><span style="color:#89DDFF">:</span><span style="color:#F7768E"> User is asking about Dexie query patterns.\nuser</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">How do I query exercises by multiple muscle groups in Dexie?</span><span style="color:#89DDFF">&quot;</span><span style="color:#F7768E">\nassistant</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">Let me use the dexie-db-specialist agent to provide an accurate answer based on the current Dexie.js documentation.</span><span style="color:#89DDFF">&quot;</span><span style="color:#F7768E">\n&lt;commentary&gt;\nSince the user is asking about Dexie.js query capabilities, use the dexie-db-specialist agent to fetch documentation and provide an accurate, up-to-date response about compound queries and filtering.\n&lt;/commentary&gt;\n&lt;/example&gt;\n\n&lt;example&gt;\nContext</span><span style="color:#89DDFF">:</span><span style="color:#F7768E"> User encounters a Dexie-related error.\nuser</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">I&#39;m getting &#39;ConstraintError&#39; when trying to add a workout</span><span style="color:#89DDFF">&quot;</span><span style="color:#F7768E">\nassistant</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">I&#39;ll consult the dexie-db-specialist agent to diagnose this database constraint issue.</span><span style="color:#89DDFF">&quot;</span><span style="color:#F7768E">\n&lt;commentary&gt;\nSince this is a Dexie.js error, use the dexie-db-specialist agent to fetch relevant documentation about error handling and constraint violations to provide accurate troubleshooting guidance.\n&lt;/commentary&gt;\n&lt;/example&gt;\n\n&lt;example&gt;\nContext</span><span style="color:#89DDFF">:</span><span style="color:#F7768E"> User needs to implement a reactive query.\nuser</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">The workout list should update automatically when new workouts are added</span><span style="color:#89DDFF">&quot;</span><span style="color:#F7768E">\nassistant</span><span style="color:#89DDFF">:</span><span style="color:#89DDFF"> &quot;</span><span style="color:#9ECE6A">I&#39;ll use the dexie-db-specialist agent to implement reactive queries with liveQuery.</span><span style="color:#89DDFF">&quot;</span><span style="color:#9ECE6A">\n&lt;commentary&gt;\nSince reactive data binding with Dexie requires liveQuery, use the dexie-db-specialist agent to fetch the latest documentation on liveQuery and useLiveQuery patterns for Vue integration.\n&lt;/commentary&gt;\n&lt;/example&gt;</span></span>
<span class="line"><span style="color:#F7768E">model</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> opus</span></span>
<span class="line"><span style="color:#F7768E">color</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> orange</span></span>
<span class="line"><span style="color:#89DDFF">---</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">You are an expert Dexie.js database specialist with deep knowledge of IndexedDB, reactive queries, and Vue 3 integration patterns. Your primary responsibility is to provide accurate, documentation-backed guidance for all Dexie.js implementations.</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Critical First Step</span></span>
<span class="line"></span>
<span class="line"><span style="color:#C0CAF5;font-weight:bold">**Before answering ANY Dexie.js question or implementing ANY Dexie-related code, you MUST:**</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">1.</span><span style="color:#9AA5CE"> Fetch the documentation index from </span><span style="color:#89DDFF">`https://dexie.org/llms.txt`</span><span style="color:#9AA5CE"> to understand the available documentation structure</span></span>
<span class="line"><span style="color:#89DDFF">2.</span><span style="color:#9AA5CE"> Based on the task at hand, fetch the relevant documentation pages to ensure your guidance is accurate and up-to-date</span></span>
<span class="line"><span style="color:#89DDFF">3.</span><span style="color:#9AA5CE"> Only then proceed with implementation or answering questions</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">This is non-negotiable. Dexie.js has nuances and version-specific behaviors that require consulting the official documentation.</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Your Expertise Covers</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#C0CAF5;font-weight:bold"> **Schema Design**</span><span style="color:#9AA5CE">: Table definitions, indexes (simple, compound, multi-entry), primary keys, version migrations</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#C0CAF5;font-weight:bold"> **CRUD Operations**</span><span style="color:#9AA5CE">: add(), put(), update(), delete(), bulkAdd(), bulkPut()</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#C0CAF5;font-weight:bold"> **Querying**</span><span style="color:#9AA5CE">: where(), filter(), equals(), between(), anyOf(), startsWithIgnoreCase(), compound queries</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#C0CAF5;font-weight:bold"> **Reactive Queries**</span><span style="color:#9AA5CE">: liveQuery() for real-time updates, integration with Vue&#39;s reactivity system</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#C0CAF5;font-weight:bold"> **Transactions**</span><span style="color:#9AA5CE">: Transaction scopes, nested transactions, error handling within transactions</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#C0CAF5;font-weight:bold"> **Relationships**</span><span style="color:#9AA5CE">: Foreign keys, table relationships, populating related data</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#C0CAF5;font-weight:bold"> **Performance**</span><span style="color:#9AA5CE">: Indexing strategies, query optimization, bulk operations</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#C0CAF5;font-weight:bold"> **Error Handling**</span><span style="color:#9AA5CE">: Dexie-specific errors (ConstraintError, AbortError, etc.)</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Project Context</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">You are working within a Vue 3 PWA workout tracker that uses:</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#C0CAF5;font-weight:bold"> **Dexie.js**</span><span style="color:#9AA5CE"> with IndexedDB for offline-first data persistence</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#C0CAF5;font-weight:bold"> **TypeScript**</span><span style="color:#9AA5CE"> with strict mode</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#C0CAF5;font-weight:bold"> **Repository pattern**</span><span style="color:#9AA5CE"> in </span><span style="color:#89DDFF">`src/db/`</span><span style="color:#9AA5CE"> for database access abstraction</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#C0CAF5;font-weight:bold"> **Pinia stores**</span><span style="color:#9AA5CE"> that consume repositories</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">When implementing, ensure your code:</span></span>
<span class="line"><span style="color:#89DDFF">1.</span><span style="color:#9AA5CE"> Follows the existing repository pattern in </span><span style="color:#89DDFF">`src/db/`</span></span>
<span class="line"><span style="color:#89DDFF">2.</span><span style="color:#9AA5CE"> Uses TypeScript interfaces for table schemas</span></span>
<span class="line"><span style="color:#89DDFF">3.</span><span style="color:#9AA5CE"> Integrates properly with Vue 3 reactivity (useLiveQuery from @vueuse/rxjs or similar)</span></span>
<span class="line"><span style="color:#89DDFF">4.</span><span style="color:#9AA5CE"> Handles errors gracefully with proper typing</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Documentation Fetching Strategy</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">When fetching from </span><span style="color:#89DDFF">`https://dexie.org/llms.txt`</span><span style="color:#9AA5CE">:</span></span>
<span class="line"><span style="color:#89DDFF">1.</span><span style="color:#9AA5CE"> Parse the sitemap to identify relevant documentation pages</span></span>
<span class="line"><span style="color:#89DDFF">2.</span><span style="color:#9AA5CE"> Fetch specific pages based on the task (e.g., for queries, fetch the WhereClause and Collection docs)</span></span>
<span class="line"><span style="color:#89DDFF">3.</span><span style="color:#9AA5CE"> Cross-reference multiple pages when dealing with complex topics</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">Common documentation sections to reference:</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#89DDFF"> `/docs/Table/Table`</span><span style="color:#9AA5CE"> - Core table operations</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#89DDFF"> `/docs/WhereClause/WhereClause`</span><span style="color:#9AA5CE"> - Query building</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#89DDFF"> `/docs/Collection/Collection`</span><span style="color:#9AA5CE"> - Result set operations</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#89DDFF"> `/docs/liveQuery()`</span><span style="color:#9AA5CE"> - Reactive queries</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#89DDFF"> `/docs/Dexie/Dexie`</span><span style="color:#9AA5CE"> - Database instance configuration</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#89DDFF"> `/docs/Version/Version`</span><span style="color:#9AA5CE"> - Schema migrations</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Response Format</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">When providing implementations:</span></span>
<span class="line"><span style="color:#89DDFF">1.</span><span style="color:#C0CAF5;font-weight:bold"> **Cite the documentation**</span><span style="color:#9AA5CE"> you consulted</span></span>
<span class="line"><span style="color:#89DDFF">2.</span><span style="color:#C0CAF5;font-weight:bold"> **Explain the approach**</span><span style="color:#9AA5CE"> before showing code</span></span>
<span class="line"><span style="color:#89DDFF">3.</span><span style="color:#C0CAF5;font-weight:bold"> **Provide TypeScript code**</span><span style="color:#9AA5CE"> that follows project conventions</span></span>
<span class="line"><span style="color:#89DDFF">4.</span><span style="color:#C0CAF5;font-weight:bold"> **Include error handling**</span><span style="color:#9AA5CE"> appropriate to the operation</span></span>
<span class="line"><span style="color:#89DDFF">5.</span><span style="color:#C0CAF5;font-weight:bold"> **Note any caveats**</span><span style="color:#9AA5CE"> or version-specific behaviors</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Quality Assurance</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Always verify your suggestions against the fetched documentation</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> If documentation is unclear or unavailable, explicitly state this and provide your best guidance with appropriate caveats</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> When multiple approaches exist, explain trade-offs</span></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> Consider IndexedDB limitations (no full-text search, storage limits, etc.)</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">Remember: Your value is in providing documentation-verified, accurate Dexie.js guidance. Never guess about API specifics—always fetch and verify first.</span></span>
<span class="line"></span></code><button type="button" class="copy" data-code="---
name: dexie-db-specialist
description: Use this agent when the task involves Dexie.js or IndexedDB in any way - implementing, modifying, querying, reviewing, or improving database code. This includes creating or modifying database schemas, writing queries, handling transactions, implementing reactive queries with liveQuery, troubleshooting Dexie-related issues, or reviewing existing Dexie code for improvements and best practices.\n\nExamples:\n\n<example>\nContext: User asks about improving their Dexie.js code.\nuser: &#34;What can I improve on this codebase when it comes to Dexie?&#34;\nassistant: &#34;I'll use the dexie-db-specialist agent to review your Dexie.js implementation against current best practices.&#34;\n<commentary>\nSince the user is asking about Dexie.js improvements, use the dexie-db-specialist agent to fetch the latest documentation and review the existing code for optimization opportunities, missing features, and best practice violations.\n</commentary>\n</example>\n\n<example>\nContext: User needs to add a new table to the database.\nuser: &#34;I need to add a new 'goals' table to track workout goals&#34;\nassistant: &#34;I'll use the dexie-db-specialist agent to implement this correctly.&#34;\n<commentary>\nSince the user needs to modify the Dexie database schema, use the dexie-db-specialist agent to first fetch the latest Dexie.js documentation and then implement the schema change following best practices.\n</commentary>\n</example>\n\n<example>\nContext: User is asking about Dexie query patterns.\nuser: &#34;How do I query exercises by multiple muscle groups in Dexie?&#34;\nassistant: &#34;Let me use the dexie-db-specialist agent to provide an accurate answer based on the current Dexie.js documentation.&#34;\n<commentary>\nSince the user is asking about Dexie.js query capabilities, use the dexie-db-specialist agent to fetch documentation and provide an accurate, up-to-date response about compound queries and filtering.\n</commentary>\n</example>\n\n<example>\nContext: User encounters a Dexie-related error.\nuser: &#34;I'm getting 'ConstraintError' when trying to add a workout&#34;\nassistant: &#34;I'll consult the dexie-db-specialist agent to diagnose this database constraint issue.&#34;\n<commentary>\nSince this is a Dexie.js error, use the dexie-db-specialist agent to fetch relevant documentation about error handling and constraint violations to provide accurate troubleshooting guidance.\n</commentary>\n</example>\n\n<example>\nContext: User needs to implement a reactive query.\nuser: &#34;The workout list should update automatically when new workouts are added&#34;\nassistant: &#34;I'll use the dexie-db-specialist agent to implement reactive queries with liveQuery.&#34;\n<commentary>\nSince reactive data binding with Dexie requires liveQuery, use the dexie-db-specialist agent to fetch the latest documentation on liveQuery and useLiveQuery patterns for Vue integration.\n</commentary>\n</example>
model: opus
color: orange
---

You are an expert Dexie.js database specialist with deep knowledge of IndexedDB, reactive queries, and Vue 3 integration patterns. Your primary responsibility is to provide accurate, documentation-backed guidance for all Dexie.js implementations.

## Critical First Step

**Before answering ANY Dexie.js question or implementing ANY Dexie-related code, you MUST:**

1. Fetch the documentation index from `https://dexie.org/llms.txt` to understand the available documentation structure
2. Based on the task at hand, fetch the relevant documentation pages to ensure your guidance is accurate and up-to-date
3. Only then proceed with implementation or answering questions

This is non-negotiable. Dexie.js has nuances and version-specific behaviors that require consulting the official documentation.

## Your Expertise Covers

- **Schema Design**: Table definitions, indexes (simple, compound, multi-entry), primary keys, version migrations
- **CRUD Operations**: add(), put(), update(), delete(), bulkAdd(), bulkPut()
- **Querying**: where(), filter(), equals(), between(), anyOf(), startsWithIgnoreCase(), compound queries
- **Reactive Queries**: liveQuery() for real-time updates, integration with Vue's reactivity system
- **Transactions**: Transaction scopes, nested transactions, error handling within transactions
- **Relationships**: Foreign keys, table relationships, populating related data
- **Performance**: Indexing strategies, query optimization, bulk operations
- **Error Handling**: Dexie-specific errors (ConstraintError, AbortError, etc.)

## Project Context

You are working within a Vue 3 PWA workout tracker that uses:
- **Dexie.js** with IndexedDB for offline-first data persistence
- **TypeScript** with strict mode
- **Repository pattern** in `src/db/` for database access abstraction
- **Pinia stores** that consume repositories

When implementing, ensure your code:
1. Follows the existing repository pattern in `src/db/`
2. Uses TypeScript interfaces for table schemas
3. Integrates properly with Vue 3 reactivity (useLiveQuery from @vueuse/rxjs or similar)
4. Handles errors gracefully with proper typing

## Documentation Fetching Strategy

When fetching from `https://dexie.org/llms.txt`:
1. Parse the sitemap to identify relevant documentation pages
2. Fetch specific pages based on the task (e.g., for queries, fetch the WhereClause and Collection docs)
3. Cross-reference multiple pages when dealing with complex topics

Common documentation sections to reference:
- `/docs/Table/Table` - Core table operations
- `/docs/WhereClause/WhereClause` - Query building
- `/docs/Collection/Collection` - Result set operations
- `/docs/liveQuery()` - Reactive queries
- `/docs/Dexie/Dexie` - Database instance configuration
- `/docs/Version/Version` - Schema migrations

## Response Format

When providing implementations:
1. **Cite the documentation** you consulted
2. **Explain the approach** before showing code
3. **Provide TypeScript code** that follows project conventions
4. **Include error handling** appropriate to the operation
5. **Note any caveats** or version-specific behaviors

## Quality Assurance

- Always verify your suggestions against the fetched documentation
- If documentation is unclear or unavailable, explicitly state this and provide your best guidance with appropriate caveats
- When multiple approaches exist, explain trade-offs
- Consider IndexedDB limitations (no full-text search, storage limits, etc.)

Remember: Your value is in providing documentation-verified, accurate Dexie.js guidance. Never guess about API specifics—always fetch and verify first.
" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre> </div> </details>  
<h3 id="what-happens-2">What Happens<a class="heading-link" aria-label="Link to section" href="#what-happens-2"><span class="heading-link-icon">#</span></a></h3>
<p>When you ask about Dexie, Claude automatically recognizes this as a database task and delegates to the specialist. The specialist works in <strong>its own context window</strong>, fetches the docs, does the work, and returns results to your main conversation.</p>
<p><svg id="mermaid-1" width="850" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" height="593" viewBox="-50 -10 850 593" role="graphics-document document" aria-roledescription="sequence"><g><rect x="600" y="507" fill="#eaeaea" stroke="#666" width="150" height="65" name="Web" rx="3" ry="3" class="actor actor-bottom"></rect><text x="675" y="539.5" dominant-baseline="central" alignment-baseline="central" class="actor actor-box" style="text-anchor:middle;font-size:16px;font-weight:400;font-family:arial, sans-serif"><tspan x="675" dy="0">dexie.org</tspan></text></g><g><rect x="400" y="507" fill="#eaeaea" stroke="#666" width="150" height="65" name="Sub" rx="3" ry="3" class="actor actor-bottom"></rect><text x="475" y="539.5" dominant-baseline="central" alignment-baseline="central" class="actor actor-box" style="text-anchor:middle;font-size:16px;font-weight:400;font-family:arial, sans-serif"><tspan x="475" dy="0">Dexie Subagent</tspan></text></g><g><rect x="200" y="507" fill="#eaeaea" stroke="#666" width="150" height="65" name="Main" rx="3" ry="3" class="actor actor-bottom"></rect><text x="275" y="539.5" dominant-baseline="central" alignment-baseline="central" class="actor actor-box" style="text-anchor:middle;font-size:16px;font-weight:400;font-family:arial, sans-serif"><tspan x="275" dy="0">Main Claude</tspan></text></g><g><rect x="0" y="507" fill="#eaeaea" stroke="#666" width="150" height="65" name="User" rx="3" ry="3" class="actor actor-bottom"></rect><text x="75" y="539.5" dominant-baseline="central" alignment-baseline="central" class="actor actor-box" style="text-anchor:middle;font-size:16px;font-weight:400;font-family:arial, sans-serif"><tspan x="75" dy="0">User</tspan></text></g><g><line id="actor3" x1="675" y1="65" x2="675" y2="507" class="actor-line 200" stroke-width="0.5px" stroke="#999" name="Web"></line><g id="root-3"><rect x="600" y="0" fill="#eaeaea" stroke="#666" width="150" height="65" name="Web" rx="3" ry="3" class="actor actor-top"></rect><text x="675" y="32.5" dominant-baseline="central" alignment-baseline="central" class="actor actor-box" style="text-anchor:middle;font-size:16px;font-weight:400;font-family:arial, sans-serif"><tspan x="675" dy="0">dexie.org</tspan></text></g></g><g><line id="actor2" x1="475" y1="65" x2="475" y2="507" class="actor-line 200" stroke-width="0.5px" stroke="#999" name="Sub"></line><g id="root-2"><rect x="400" y="0" fill="#eaeaea" stroke="#666" width="150" height="65" name="Sub" rx="3" ry="3" class="actor actor-top"></rect><text x="475" y="32.5" dominant-baseline="central" alignment-baseline="central" class="actor actor-box" style="text-anchor:middle;font-size:16px;font-weight:400;font-family:arial, sans-serif"><tspan x="475" dy="0">Dexie Subagent</tspan></text></g></g><g><line id="actor1" x1="275" y1="65" x2="275" y2="507" class="actor-line 200" stroke-width="0.5px" stroke="#999" name="Main"></line><g id="root-1"><rect x="200" y="0" fill="#eaeaea" stroke="#666" width="150" height="65" name="Main" rx="3" ry="3" class="actor actor-top"></rect><text x="275" y="32.5" dominant-baseline="central" alignment-baseline="central" class="actor actor-box" style="text-anchor:middle;font-size:16px;font-weight:400;font-family:arial, sans-serif"><tspan x="275" dy="0">Main Claude</tspan></text></g></g><g><line id="actor0" x1="75" y1="65" x2="75" y2="507" class="actor-line 200" stroke-width="0.5px" stroke="#999" name="User"></line><g id="root-0"><rect x="0" y="0" fill="#eaeaea" stroke="#666" width="150" height="65" name="User" rx="3" ry="3" class="actor actor-top"></rect><text x="75" y="32.5" dominant-baseline="central" alignment-baseline="central" class="actor actor-box" style="text-anchor:middle;font-size:16px;font-weight:400;font-family:arial, sans-serif"><tspan x="75" dy="0">User</tspan></text></g></g><style>#mermaid-1{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;fill:#ccc;}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#mermaid-1 .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#mermaid-1 .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#mermaid-1 .error-icon{fill:#a44141;}#mermaid-1 .error-text{fill:#ddd;stroke:#ddd;}#mermaid-1 .edge-thickness-normal{stroke-width:1px;}#mermaid-1 .edge-thickness-thick{stroke-width:3.5px;}#mermaid-1 .edge-pattern-solid{stroke-dasharray:0;}#mermaid-1 .edge-thickness-invisible{stroke-width:0;fill:none;}#mermaid-1 .edge-pattern-dashed{stroke-dasharray:3;}#mermaid-1 .edge-pattern-dotted{stroke-dasharray:2;}#mermaid-1 .marker{fill:rgb(171, 75, 153);stroke:rgb(171, 75, 153);}#mermaid-1 .marker.cross{stroke:rgb(171, 75, 153);}#mermaid-1 svg{font-family:ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,"Liberation Mono","Courier New",monospace;font-size:16px;}#mermaid-1 p{margin:0;}#mermaid-1 .actor{stroke:#ccc;fill:transparent;}#mermaid-1 text.actor>tspan{fill:lightgrey;stroke:none;}#mermaid-1 .actor-line{stroke:#ccc;}#mermaid-1 .innerArc{stroke-width:1.5;stroke-dasharray:none;}#mermaid-1 .messageLine0{stroke-width:1.5;stroke-dasharray:none;stroke:lightgrey;}#mermaid-1 .messageLine1{stroke-width:1.5;stroke-dasharray:2,2;stroke:lightgrey;}#mermaid-1 #arrowhead path{fill:lightgrey;stroke:lightgrey;}#mermaid-1 .sequenceNumber{fill:black;}#mermaid-1 #sequencenumber{fill:lightgrey;}#mermaid-1 #crosshead path{fill:lightgrey;stroke:lightgrey;}#mermaid-1 .messageText{fill:lightgrey;stroke:none;}#mermaid-1 .labelBox{stroke:#ccc;fill:transparent;}#mermaid-1 .labelText,#mermaid-1 .labelText>tspan{fill:lightgrey;stroke:none;}#mermaid-1 .loopText,#mermaid-1 .loopText>tspan{fill:lightgrey;stroke:none;}#mermaid-1 .loopLine{stroke-width:2px;stroke-dasharray:2,2;stroke:#ccc;fill:#ccc;}#mermaid-1 .note{stroke:hsl(180, 0%, 18.3529411765%);fill:hsla(0, 0%, 16%, 0);}#mermaid-1 .noteText,#mermaid-1 .noteText>tspan{fill:rgb(183.8476190475, 181.5523809523, 181.5523809523);stroke:none;}#mermaid-1 .activation0{fill:hsla(0, 0%, 16%, 0);stroke:#ccc;}#mermaid-1 .activation1{fill:hsla(0, 0%, 16%, 0);stroke:#ccc;}#mermaid-1 .activation2{fill:hsla(0, 0%, 16%, 0);stroke:#ccc;}#mermaid-1 .actorPopupMenu{position:absolute;}#mermaid-1 .actorPopupMenuPanel{position:absolute;fill:transparent;box-shadow:0px 8px 16px 0px rgba(0,0,0,0.2);filter:drop-shadow(3px 5px 2px rgb(0 0 0 / 0.4));}#mermaid-1 .actor-man line{stroke:#ccc;fill:transparent;}#mermaid-1 .actor-man circle,#mermaid-1 line{stroke:#ccc;fill:transparent;stroke-width:2px;}#mermaid-1 :root{--mermaid-font-family:arial,sans-serif;}</style><g></g><defs><symbol id="computer" width="24" height="24"><path transform="scale(.5)" d="M2 2v13h20v-13h-20zm18 11h-16v-9h16v9zm-10.228 6l.466-1h3.524l.467 1h-4.457zm14.228 3h-24l2-6h2.104l-1.33 4h18.45l-1.297-4h2.073l2 6zm-5-10h-14v-7h14v7z"></path></symbol></defs><defs><symbol id="database" fill-rule="evenodd" clip-rule="evenodd"><path transform="scale(.5)" d="M12.258.001l.256.004.255.005.253.008.251.01.249.012.247.015.246.016.242.019.241.02.239.023.236.024.233.027.231.028.229.031.225.032.223.034.22.036.217.038.214.04.211.041.208.043.205.045.201.046.198.048.194.05.191.051.187.053.183.054.18.056.175.057.172.059.168.06.163.061.16.063.155.064.15.066.074.033.073.033.071.034.07.034.069.035.068.035.067.035.066.035.064.036.064.036.062.036.06.036.06.037.058.037.058.037.055.038.055.038.053.038.052.038.051.039.05.039.048.039.047.039.045.04.044.04.043.04.041.04.04.041.039.041.037.041.036.041.034.041.033.042.032.042.03.042.029.042.027.042.026.043.024.043.023.043.021.043.02.043.018.044.017.043.015.044.013.044.012.044.011.045.009.044.007.045.006.045.004.045.002.045.001.045v17l-.001.045-.002.045-.004.045-.006.045-.007.045-.009.044-.011.045-.012.044-.013.044-.015.044-.017.043-.018.044-.02.043-.021.043-.023.043-.024.043-.026.043-.027.042-.029.042-.03.042-.032.042-.033.042-.034.041-.036.041-.037.041-.039.041-.04.041-.041.04-.043.04-.044.04-.045.04-.047.039-.048.039-.05.039-.051.039-.052.038-.053.038-.055.038-.055.038-.058.037-.058.037-.06.037-.06.036-.062.036-.064.036-.064.036-.066.035-.067.035-.068.035-.069.035-.07.034-.071.034-.073.033-.074.033-.15.066-.155.064-.16.063-.163.061-.168.06-.172.059-.175.057-.18.056-.183.054-.187.053-.191.051-.194.05-.198.048-.201.046-.205.045-.208.043-.211.041-.214.04-.217.038-.22.036-.223.034-.225.032-.229.031-.231.028-.233.027-.236.024-.239.023-.241.02-.242.019-.246.016-.247.015-.249.012-.251.01-.253.008-.255.005-.256.004-.258.001-.258-.001-.256-.004-.255-.005-.253-.008-.251-.01-.249-.012-.247-.015-.245-.016-.243-.019-.241-.02-.238-.023-.236-.024-.234-.027-.231-.028-.228-.031-.226-.032-.223-.034-.22-.036-.217-.038-.214-.04-.211-.041-.208-.043-.204-.045-.201-.046-.198-.048-.195-.05-.19-.051-.187-.053-.184-.054-.179-.056-.176-.057-.172-.059-.167-.06-.164-.061-.159-.063-.155-.064-.151-.066-.074-.033-.072-.033-.072-.034-.07-.034-.069-.035-.068-.035-.067-.035-.066-.035-.064-.036-.063-.036-.062-.036-.061-.036-.06-.037-.058-.037-.057-.037-.056-.038-.055-.038-.053-.038-.052-.038-.051-.039-.049-.039-.049-.039-.046-.039-.046-.04-.044-.04-.043-.04-.041-.04-.04-.041-.039-.041-.037-.041-.036-.041-.034-.041-.033-.042-.032-.042-.03-.042-.029-.042-.027-.042-.026-.043-.024-.043-.023-.043-.021-.043-.02-.043-.018-.044-.017-.043-.015-.044-.013-.044-.012-.044-.011-.045-.009-.044-.007-.045-.006-.045-.004-.045-.002-.045-.001-.045v-17l.001-.045.002-.045.004-.045.006-.045.007-.045.009-.044.011-.045.012-.044.013-.044.015-.044.017-.043.018-.044.02-.043.021-.043.023-.043.024-.043.026-.043.027-.042.029-.042.03-.042.032-.042.033-.042.034-.041.036-.041.037-.041.039-.041.04-.041.041-.04.043-.04.044-.04.046-.04.046-.039.049-.039.049-.039.051-.039.052-.038.053-.038.055-.038.056-.038.057-.037.058-.037.06-.037.061-.036.062-.036.063-.036.064-.036.066-.035.067-.035.068-.035.069-.035.07-.034.072-.034.072-.033.074-.033.151-.066.155-.064.159-.063.164-.061.167-.06.172-.059.176-.057.179-.056.184-.054.187-.053.19-.051.195-.05.198-.048.201-.046.204-.045.208-.043.211-.041.214-.04.217-.038.22-.036.223-.034.226-.032.228-.031.231-.028.234-.027.236-.024.238-.023.241-.02.243-.019.245-.016.247-.015.249-.012.251-.01.253-.008.255-.005.256-.004.258-.001.258.001zm-9.258 20.499v.01l.001.021.003.021.004.022.005.021.006.022.007.022.009.023.01.022.011.023.012.023.013.023.015.023.016.024.017.023.018.024.019.024.021.024.022.025.023.024.024.025.052.049.056.05.061.051.066.051.07.051.075.051.079.052.084.052.088.052.092.052.097.052.102.051.105.052.11.052.114.051.119.051.123.051.127.05.131.05.135.05.139.048.144.049.147.047.152.047.155.047.16.045.163.045.167.043.171.043.176.041.178.041.183.039.187.039.19.037.194.035.197.035.202.033.204.031.209.03.212.029.216.027.219.025.222.024.226.021.23.02.233.018.236.016.24.015.243.012.246.01.249.008.253.005.256.004.259.001.26-.001.257-.004.254-.005.25-.008.247-.011.244-.012.241-.014.237-.016.233-.018.231-.021.226-.021.224-.024.22-.026.216-.027.212-.028.21-.031.205-.031.202-.034.198-.034.194-.036.191-.037.187-.039.183-.04.179-.04.175-.042.172-.043.168-.044.163-.045.16-.046.155-.046.152-.047.148-.048.143-.049.139-.049.136-.05.131-.05.126-.05.123-.051.118-.052.114-.051.11-.052.106-.052.101-.052.096-.052.092-.052.088-.053.083-.051.079-.052.074-.052.07-.051.065-.051.06-.051.056-.05.051-.05.023-.024.023-.025.021-.024.02-.024.019-.024.018-.024.017-.024.015-.023.014-.024.013-.023.012-.023.01-.023.01-.022.008-.022.006-.022.006-.022.004-.022.004-.021.001-.021.001-.021v-4.127l-.077.055-.08.053-.083.054-.085.053-.087.052-.09.052-.093.051-.095.05-.097.05-.1.049-.102.049-.105.048-.106.047-.109.047-.111.046-.114.045-.115.045-.118.044-.12.043-.122.042-.124.042-.126.041-.128.04-.13.04-.132.038-.134.038-.135.037-.138.037-.139.035-.142.035-.143.034-.144.033-.147.032-.148.031-.15.03-.151.03-.153.029-.154.027-.156.027-.158.026-.159.025-.161.024-.162.023-.163.022-.165.021-.166.02-.167.019-.169.018-.169.017-.171.016-.173.015-.173.014-.175.013-.175.012-.177.011-.178.01-.179.008-.179.008-.181.006-.182.005-.182.004-.184.003-.184.002h-.37l-.184-.002-.184-.003-.182-.004-.182-.005-.181-.006-.179-.008-.179-.008-.178-.01-.176-.011-.176-.012-.175-.013-.173-.014-.172-.015-.171-.016-.17-.017-.169-.018-.167-.019-.166-.02-.165-.021-.163-.022-.162-.023-.161-.024-.159-.025-.157-.026-.156-.027-.155-.027-.153-.029-.151-.03-.15-.03-.148-.031-.146-.032-.145-.033-.143-.034-.141-.035-.14-.035-.137-.037-.136-.037-.134-.038-.132-.038-.13-.04-.128-.04-.126-.041-.124-.042-.122-.042-.12-.044-.117-.043-.116-.045-.113-.045-.112-.046-.109-.047-.106-.047-.105-.048-.102-.049-.1-.049-.097-.05-.095-.05-.093-.052-.09-.051-.087-.052-.085-.053-.083-.054-.08-.054-.077-.054v4.127zm0-5.654v.011l.001.021.003.021.004.021.005.022.006.022.007.022.009.022.01.022.011.023.012.023.013.023.015.024.016.023.017.024.018.024.019.024.021.024.022.024.023.025.024.024.052.05.056.05.061.05.066.051.07.051.075.052.079.051.084.052.088.052.092.052.097.052.102.052.105.052.11.051.114.051.119.052.123.05.127.051.131.05.135.049.139.049.144.048.147.048.152.047.155.046.16.045.163.045.167.044.171.042.176.042.178.04.183.04.187.038.19.037.194.036.197.034.202.033.204.032.209.03.212.028.216.027.219.025.222.024.226.022.23.02.233.018.236.016.24.014.243.012.246.01.249.008.253.006.256.003.259.001.26-.001.257-.003.254-.006.25-.008.247-.01.244-.012.241-.015.237-.016.233-.018.231-.02.226-.022.224-.024.22-.025.216-.027.212-.029.21-.03.205-.032.202-.033.198-.035.194-.036.191-.037.187-.039.183-.039.179-.041.175-.042.172-.043.168-.044.163-.045.16-.045.155-.047.152-.047.148-.048.143-.048.139-.05.136-.049.131-.05.126-.051.123-.051.118-.051.114-.052.11-.052.106-.052.101-.052.096-.052.092-.052.088-.052.083-.052.079-.052.074-.051.07-.052.065-.051.06-.05.056-.051.051-.049.023-.025.023-.024.021-.025.02-.024.019-.024.018-.024.017-.024.015-.023.014-.023.013-.024.012-.022.01-.023.01-.023.008-.022.006-.022.006-.022.004-.021.004-.022.001-.021.001-.021v-4.139l-.077.054-.08.054-.083.054-.085.052-.087.053-.09.051-.093.051-.095.051-.097.05-.1.049-.102.049-.105.048-.106.047-.109.047-.111.046-.114.045-.115.044-.118.044-.12.044-.122.042-.124.042-.126.041-.128.04-.13.039-.132.039-.134.038-.135.037-.138.036-.139.036-.142.035-.143.033-.144.033-.147.033-.148.031-.15.03-.151.03-.153.028-.154.028-.156.027-.158.026-.159.025-.161.024-.162.023-.163.022-.165.021-.166.02-.167.019-.169.018-.169.017-.171.016-.173.015-.173.014-.175.013-.175.012-.177.011-.178.009-.179.009-.179.007-.181.007-.182.005-.182.004-.184.003-.184.002h-.37l-.184-.002-.184-.003-.182-.004-.182-.005-.181-.007-.179-.007-.179-.009-.178-.009-.176-.011-.176-.012-.175-.013-.173-.014-.172-.015-.171-.016-.17-.017-.169-.018-.167-.019-.166-.02-.165-.021-.163-.022-.162-.023-.161-.024-.159-.025-.157-.026-.156-.027-.155-.028-.153-.028-.151-.03-.15-.03-.148-.031-.146-.033-.145-.033-.143-.033-.141-.035-.14-.036-.137-.036-.136-.037-.134-.038-.132-.039-.13-.039-.128-.04-.126-.041-.124-.042-.122-.043-.12-.043-.117-.044-.116-.044-.113-.046-.112-.046-.109-.046-.106-.047-.105-.048-.102-.049-.1-.049-.097-.05-.095-.051-.093-.051-.09-.051-.087-.053-.085-.052-.083-.054-.08-.054-.077-.054v4.139zm0-5.666v.011l.001.02.003.022.004.021.005.022.006.021.007.022.009.023.01.022.011.023.012.023.013.023.015.023.016.024.017.024.018.023.019.024.021.025.022.024.023.024.024.025.052.05.056.05.061.05.066.051.07.051.075.052.079.051.084.052.088.052.092.052.097.052.102.052.105.051.11.052.114.051.119.051.123.051.127.05.131.05.135.05.139.049.144.048.147.048.152.047.155.046.16.045.163.045.167.043.171.043.176.042.178.04.183.04.187.038.19.037.194.036.197.034.202.033.204.032.209.03.212.028.216.027.219.025.222.024.226.021.23.02.233.018.236.017.24.014.243.012.246.01.249.008.253.006.256.003.259.001.26-.001.257-.003.254-.006.25-.008.247-.01.244-.013.241-.014.237-.016.233-.018.231-.02.226-.022.224-.024.22-.025.216-.027.212-.029.21-.03.205-.032.202-.033.198-.035.194-.036.191-.037.187-.039.183-.039.179-.041.175-.042.172-.043.168-.044.163-.045.16-.045.155-.047.152-.047.148-.048.143-.049.139-.049.136-.049.131-.051.126-.05.123-.051.118-.052.114-.051.11-.052.106-.052.101-.052.096-.052.092-.052.088-.052.083-.052.079-.052.074-.052.07-.051.065-.051.06-.051.056-.05.051-.049.023-.025.023-.025.021-.024.02-.024.019-.024.018-.024.017-.024.015-.023.014-.024.013-.023.012-.023.01-.022.01-.023.008-.022.006-.022.006-.022.004-.022.004-.021.001-.021.001-.021v-4.153l-.077.054-.08.054-.083.053-.085.053-.087.053-.09.051-.093.051-.095.051-.097.05-.1.049-.102.048-.105.048-.106.048-.109.046-.111.046-.114.046-.115.044-.118.044-.12.043-.122.043-.124.042-.126.041-.128.04-.13.039-.132.039-.134.038-.135.037-.138.036-.139.036-.142.034-.143.034-.144.033-.147.032-.148.032-.15.03-.151.03-.153.028-.154.028-.156.027-.158.026-.159.024-.161.024-.162.023-.163.023-.165.021-.166.02-.167.019-.169.018-.169.017-.171.016-.173.015-.173.014-.175.013-.175.012-.177.01-.178.01-.179.009-.179.007-.181.006-.182.006-.182.004-.184.003-.184.001-.185.001-.185-.001-.184-.001-.184-.003-.182-.004-.182-.006-.181-.006-.179-.007-.179-.009-.178-.01-.176-.01-.176-.012-.175-.013-.173-.014-.172-.015-.171-.016-.17-.017-.169-.018-.167-.019-.166-.02-.165-.021-.163-.023-.162-.023-.161-.024-.159-.024-.157-.026-.156-.027-.155-.028-.153-.028-.151-.03-.15-.03-.148-.032-.146-.032-.145-.033-.143-.034-.141-.034-.14-.036-.137-.036-.136-.037-.134-.038-.132-.039-.13-.039-.128-.041-.126-.041-.124-.041-.122-.043-.12-.043-.117-.044-.116-.044-.113-.046-.112-.046-.109-.046-.106-.048-.105-.048-.102-.048-.1-.05-.097-.049-.095-.051-.093-.051-.09-.052-.087-.052-.085-.053-.083-.053-.08-.054-.077-.054v4.153zm8.74-8.179l-.257.004-.254.005-.25.008-.247.011-.244.012-.241.014-.237.016-.233.018-.231.021-.226.022-.224.023-.22.026-.216.027-.212.028-.21.031-.205.032-.202.033-.198.034-.194.036-.191.038-.187.038-.183.04-.179.041-.175.042-.172.043-.168.043-.163.045-.16.046-.155.046-.152.048-.148.048-.143.048-.139.049-.136.05-.131.05-.126.051-.123.051-.118.051-.114.052-.11.052-.106.052-.101.052-.096.052-.092.052-.088.052-.083.052-.079.052-.074.051-.07.052-.065.051-.06.05-.056.05-.051.05-.023.025-.023.024-.021.024-.02.025-.019.024-.018.024-.017.023-.015.024-.014.023-.013.023-.012.023-.01.023-.01.022-.008.022-.006.023-.006.021-.004.022-.004.021-.001.021-.001.021.001.021.001.021.004.021.004.022.006.021.006.023.008.022.01.022.01.023.012.023.013.023.014.023.015.024.017.023.018.024.019.024.02.025.021.024.023.024.023.025.051.05.056.05.06.05.065.051.07.052.074.051.079.052.083.052.088.052.092.052.096.052.101.052.106.052.11.052.114.052.118.051.123.051.126.051.131.05.136.05.139.049.143.048.148.048.152.048.155.046.16.046.163.045.168.043.172.043.175.042.179.041.183.04.187.038.191.038.194.036.198.034.202.033.205.032.21.031.212.028.216.027.22.026.224.023.226.022.231.021.233.018.237.016.241.014.244.012.247.011.25.008.254.005.257.004.26.001.26-.001.257-.004.254-.005.25-.008.247-.011.244-.012.241-.014.237-.016.233-.018.231-.021.226-.022.224-.023.22-.026.216-.027.212-.028.21-.031.205-.032.202-.033.198-.034.194-.036.191-.038.187-.038.183-.04.179-.041.175-.042.172-.043.168-.043.163-.045.16-.046.155-.046.152-.048.148-.048.143-.048.139-.049.136-.05.131-.05.126-.051.123-.051.118-.051.114-.052.11-.052.106-.052.101-.052.096-.052.092-.052.088-.052.083-.052.079-.052.074-.051.07-.052.065-.051.06-.05.056-.05.051-.05.023-.025.023-.024.021-.024.02-.025.019-.024.018-.024.017-.023.015-.024.014-.023.013-.023.012-.023.01-.023.01-.022.008-.022.006-.023.006-.021.004-.022.004-.021.001-.021.001-.021-.001-.021-.001-.021-.004-.021-.004-.022-.006-.021-.006-.023-.008-.022-.01-.022-.01-.023-.012-.023-.013-.023-.014-.023-.015-.024-.017-.023-.018-.024-.019-.024-.02-.025-.021-.024-.023-.024-.023-.025-.051-.05-.056-.05-.06-.05-.065-.051-.07-.052-.074-.051-.079-.052-.083-.052-.088-.052-.092-.052-.096-.052-.101-.052-.106-.052-.11-.052-.114-.052-.118-.051-.123-.051-.126-.051-.131-.05-.136-.05-.139-.049-.143-.048-.148-.048-.152-.048-.155-.046-.16-.046-.163-.045-.168-.043-.172-.043-.175-.042-.179-.041-.183-.04-.187-.038-.191-.038-.194-.036-.198-.034-.202-.033-.205-.032-.21-.031-.212-.028-.216-.027-.22-.026-.224-.023-.226-.022-.231-.021-.233-.018-.237-.016-.241-.014-.244-.012-.247-.011-.25-.008-.254-.005-.257-.004-.26-.001-.26.001z"></path></symbol></defs><defs><symbol id="clock" width="24" height="24"><path transform="scale(.5)" d="M12 2c5.514 0 10 4.486 10 10s-4.486 10-10 10-10-4.486-10-10 4.486-10 10-10zm0-2c-6.627 0-12 5.373-12 12s5.373 12 12 12 12-5.373 12-12-5.373-12-12-12zm5.848 12.459c.202.038.202.333.001.372-1.907.361-6.045 1.111-6.547 1.111-.719 0-1.301-.582-1.301-1.301 0-.512.77-5.447 1.125-7.445.034-.192.312-.181.343.014l.985 6.238 5.394 1.011z"></path></symbol></defs><defs><marker id="arrowhead" refX="7.9" refY="5" markerUnits="userSpaceOnUse" markerWidth="12" markerHeight="12" orient="auto-start-reverse"><path d="M -1 0 L 10 5 L 0 10 z"></path></marker></defs><defs><marker id="crosshead" markerWidth="15" markerHeight="8" orient="auto" refX="4" refY="4.5"><path fill="none" stroke="#000000" stroke-width="1pt" d="M 1,2 L 6,7 M 6,2 L 1,7" style="stroke-dasharray:0, 0"></path></marker></defs><defs><marker id="filled-head" refX="15.5" refY="7" markerWidth="20" markerHeight="28" orient="auto"><path d="M 18,7 L9,13 L14,7 L9,1 Z"></path></marker></defs><defs><marker id="sequencenumber" refX="15" refY="15" markerWidth="60" markerHeight="40" orient="auto"><circle cx="15" cy="15" r="6"></circle></marker></defs><text x="174" y="80" text-anchor="middle" dominant-baseline="middle" alignment-baseline="middle" class="messageText" dy="1em" style="font-family:arial, sans-serif;font-size:16px;font-weight:400">How do I add an index?</text><line x1="76" y1="113" x2="271" y2="113" class="messageLine0" stroke-width="2" stroke="none" marker-end="url(#arrowhead)" style="fill:none"></line><text x="374" y="128" text-anchor="middle" dominant-baseline="middle" alignment-baseline="middle" class="messageText" dy="1em" style="font-family:arial, sans-serif;font-size:16px;font-weight:400">Delegate database</text><text x="374" y="147" text-anchor="middle" dominant-baseline="middle" alignment-baseline="middle" class="messageText" dy="1em" style="font-family:arial, sans-serif;font-size:16px;font-weight:400">question</text><line x1="276" y1="180" x2="471" y2="180" class="messageLine0" stroke-width="2" stroke="none" marker-end="url(#arrowhead)" style="fill:none"></line><text x="574" y="195" text-anchor="middle" dominant-baseline="middle" alignment-baseline="middle" class="messageText" dy="1em" style="font-family:arial, sans-serif;font-size:16px;font-weight:400">Fetch llms.txt</text><line x1="476" y1="228" x2="671" y2="228" class="messageLine0" stroke-width="2" stroke="none" marker-end="url(#arrowhead)" style="fill:none"></line><text x="577" y="243" text-anchor="middle" dominant-baseline="middle" alignment-baseline="middle" class="messageText" dy="1em" style="font-family:arial, sans-serif;font-size:16px;font-weight:400">Documentation index</text><line x1="674" y1="276" x2="479" y2="276" class="messageLine1" stroke-width="2" stroke="none" marker-end="url(#arrowhead)" style="stroke-dasharray:3, 3;fill:none"></line><text x="574" y="291" text-anchor="middle" dominant-baseline="middle" alignment-baseline="middle" class="messageText" dy="1em" style="font-family:arial, sans-serif;font-size:16px;font-weight:400">Fetch relevant pages</text><line x1="476" y1="324" x2="671" y2="324" class="messageLine0" stroke-width="2" stroke="none" marker-end="url(#arrowhead)" style="fill:none"></line><text x="577" y="339" text-anchor="middle" dominant-baseline="middle" alignment-baseline="middle" class="messageText" dy="1em" style="font-family:arial, sans-serif;font-size:16px;font-weight:400">Index documentation</text><line x1="674" y1="372" x2="479" y2="372" class="messageLine1" stroke-width="2" stroke="none" marker-end="url(#arrowhead)" style="stroke-dasharray:3, 3;fill:none"></line><text x="377" y="387" text-anchor="middle" dominant-baseline="middle" alignment-baseline="middle" class="messageText" dy="1em" style="font-family:arial, sans-serif;font-size:16px;font-weight:400">Distilled answer</text><line x1="474" y1="420" x2="279" y2="420" class="messageLine1" stroke-width="2" stroke="none" marker-end="url(#arrowhead)" style="stroke-dasharray:3, 3;fill:none"></line><text x="177" y="435" text-anchor="middle" dominant-baseline="middle" alignment-baseline="middle" class="messageText" dy="1em" style="font-family:arial, sans-serif;font-size:16px;font-weight:400">Here&#39;s how to add an</text><text x="177" y="454" text-anchor="middle" dominant-baseline="middle" alignment-baseline="middle" class="messageText" dy="1em" style="font-family:arial, sans-serif;font-size:16px;font-weight:400">index...</text><line x1="274" y1="487" x2="79" y2="487" class="messageLine1" stroke-width="2" stroke="none" marker-end="url(#arrowhead)" style="stroke-dasharray:3, 3;fill:none"></line></svg></p>
<h3 id="trade-offs-2">Trade-offs<a class="heading-link" aria-label="Link to section" href="#trade-offs-2"><span class="heading-link-icon">#</span></a></h3>

























<table><thead><tr><th>✅ Pros</th><th>❌ Cons</th></tr></thead><tbody><tr><td data-label="✅ Pros">Auto-delegated when task matches</td><td data-label="❌ Cons">Heavier—launches a separate agent</td></tr><tr><td data-label="✅ Pros"><strong>Separate context window</strong>—doesn’t clutter main</td><td data-label="❌ Cons">Results come back as a summary, not live</td></tr><tr><td data-label="✅ Pros">Can use different model (e.g., opus for complex)</td><td data-label="❌ Cons">You can’t interact with the agent directly</td></tr><tr><td data-label="✅ Pros">Can restrict tools for security</td><td data-label="❌ Cons">More complex to set up</td></tr></tbody></table>
<hr/>
<h2 id="4-skills-rich-capabilities-with-auto-discovery">4. Skills: Rich Capabilities with Auto-Discovery<a class="heading-link" aria-label="Link to section" href="#4-skills-rich-capabilities-with-auto-discovery"><span class="heading-link-icon">#</span></a></h2>
<h3 id="what-it-is-3">What It Is<a class="heading-link" aria-label="Link to section" href="#what-it-is-3"><span class="heading-link-icon">#</span></a></h3>
<p>A structured capability with optional supporting files that Claude <strong>discovers automatically</strong> and uses within your main conversation.</p>
<p>Unlike simple slash commands, skills can include multiple files: reference documentation, scripts, templates, and utilities.</p>
<h3 id="where-it-lives-3">Where It Lives<a class="heading-link" aria-label="Link to section" href="#where-it-lives-3"><span class="heading-link-icon">#</span></a></h3>
<nav class="file-tree astro-htwbjus4" aria-label="File tree"> <ul class="file-tree__list astro-htwbjus4"> <li class="file-tree__item astro-o25vlg2d" style="--level: 0;"> <details class="file-tree__folder astro-o25vlg2d" open> <summary class="astro-o25vlg2d"> <span class="file-tree__caret astro-o25vlg2d" aria-hidden="true">
▸
</span> <svg class="file-tree__icon astro-o25vlg2d" aria-hidden="true" viewBox="0 0 16 16"> <path fill="currentColor" d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z" class="astro-o25vlg2d"></path> </svg> <span class="file-tree__name astro-o25vlg2d">.claude</span>  </summary> <ul class="file-tree__list astro-o25vlg2d"> <li class="file-tree__item astro-o25vlg2d" style="--level: 1;"> <details class="file-tree__folder astro-o25vlg2d" open> <summary class="astro-o25vlg2d"> <span class="file-tree__caret astro-o25vlg2d" aria-hidden="true">
▸
</span> <svg class="file-tree__icon astro-o25vlg2d" aria-hidden="true" viewBox="0 0 16 16"> <path fill="currentColor" d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z" class="astro-o25vlg2d"></path> </svg> <span class="file-tree__name astro-o25vlg2d">skills</span>  </summary> <ul class="file-tree__list astro-o25vlg2d"> <li class="file-tree__item astro-o25vlg2d" style="--level: 2;"> <details class="file-tree__folder astro-o25vlg2d" open> <summary class="astro-o25vlg2d"> <span class="file-tree__caret astro-o25vlg2d" aria-hidden="true">
▸
</span> <svg class="file-tree__icon astro-o25vlg2d" aria-hidden="true" viewBox="0 0 16 16"> <path fill="currentColor" d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z" class="astro-o25vlg2d"></path> </svg> <span class="file-tree__name astro-o25vlg2d">dexie-expert</span>  </summary> <ul class="file-tree__list astro-o25vlg2d"> <li class="file-tree__item astro-o25vlg2d" style="--level: 3;">   <span class="file-tree__file astro-o25vlg2d">  <svg class="file-tree__icon file-tree__icon--file file-tree__icon--colored astro-o25vlg2d" aria-hidden="true" viewBox="0 0 24 24"> <path fill="#519ABA" d="M22.27 19.385H1.73A1.73 1.73 0 010 17.655V6.345a1.73 1.73 0 011.73-1.73h20.54A1.73 1.73 0 0124 6.345v11.308a1.73 1.73 0 01-1.73 1.731zM5.769 15.923v-4.5l2.308 2.885 2.307-2.885v4.5h2.308V8.078h-2.308l-2.307 2.885-2.308-2.885H3.46v7.847zM21.232 12h-2.309V8.077h-2.307V12h-2.308l3.461 4.039z" class="astro-o25vlg2d"></path> </svg>  <span class="file-tree__name astro-o25vlg2d">SKILL.md</span> <span class="file-tree__comment astro-o25vlg2d">// Main definition</span> </span> </li> <li class="file-tree__item astro-o25vlg2d" style="--level: 3;">   <span class="file-tree__file astro-o25vlg2d">  <svg class="file-tree__icon file-tree__icon--file file-tree__icon--colored astro-o25vlg2d" aria-hidden="true" viewBox="0 0 24 24"> <path fill="#519ABA" d="M22.27 19.385H1.73A1.73 1.73 0 010 17.655V6.345a1.73 1.73 0 011.73-1.73h20.54A1.73 1.73 0 0124 6.345v11.308a1.73 1.73 0 01-1.73 1.731zM5.769 15.923v-4.5l2.308 2.885 2.307-2.885v4.5h2.308V8.078h-2.308l-2.307 2.885-2.308-2.885H3.46v7.847zM21.232 12h-2.309V8.077h-2.307V12h-2.308l3.461 4.039z" class="astro-o25vlg2d"></path> </svg>  <span class="file-tree__name astro-o25vlg2d">PATTERNS.md</span> <span class="file-tree__comment astro-o25vlg2d">// Common patterns</span> </span> </li> <li class="file-tree__item astro-o25vlg2d" style="--level: 3;">   <span class="file-tree__file astro-o25vlg2d">  <svg class="file-tree__icon file-tree__icon--file file-tree__icon--colored astro-o25vlg2d" aria-hidden="true" viewBox="0 0 24 24"> <path fill="#519ABA" d="M22.27 19.385H1.73A1.73 1.73 0 010 17.655V6.345a1.73 1.73 0 011.73-1.73h20.54A1.73 1.73 0 0124 6.345v11.308a1.73 1.73 0 01-1.73 1.731zM5.769 15.923v-4.5l2.308 2.885 2.307-2.885v4.5h2.308V8.078h-2.308l-2.307 2.885-2.308-2.885H3.46v7.847zM21.232 12h-2.309V8.077h-2.307V12h-2.308l3.461 4.039z" class="astro-o25vlg2d"></path> </svg>  <span class="file-tree__name astro-o25vlg2d">MIGRATIONS.md</span> <span class="file-tree__comment astro-o25vlg2d">// Migration guide</span> </span> </li> <li class="file-tree__item astro-o25vlg2d" style="--level: 3;"> <details class="file-tree__folder astro-o25vlg2d"> <summary class="astro-o25vlg2d"> <span class="file-tree__caret astro-o25vlg2d" aria-hidden="true">
▸
</span> <svg class="file-tree__icon astro-o25vlg2d" aria-hidden="true" viewBox="0 0 16 16"> <path fill="currentColor" d="M1.75 1A1.75 1.75 0 0 0 0 2.75v10.5C0 14.216.784 15 1.75 15h12.5A1.75 1.75 0 0 0 16 13.25v-8.5A1.75 1.75 0 0 0 14.25 3H7.5a.25.25 0 0 1-.2-.1l-.9-1.2C6.07 1.26 5.55 1 5 1H1.75Z" class="astro-o25vlg2d"></path> </svg> <span class="file-tree__name astro-o25vlg2d">scripts</span>  </summary> <ul class="file-tree__list astro-o25vlg2d"> <li class="file-tree__item astro-o25vlg2d" style="--level: 4;">   <span class="file-tree__file astro-o25vlg2d">  <svg class="file-tree__icon file-tree__icon--file file-tree__icon--colored astro-o25vlg2d" aria-hidden="true" viewBox="0 0 24 24"> <path fill="#3178C6" d="M1.125 0C.502 0 0 .502 0 1.125v21.75C0 23.498.502 24 1.125 24h21.75c.623 0 1.125-.502 1.125-1.125V1.125C24 .502 23.498 0 22.875 0zm17.363 9.75c.612 0 1.154.037 1.627.111a6.38 6.38 0 0 1 1.306.34v2.458a3.95 3.95 0 0 0-.643-.361 5.093 5.093 0 0 0-.717-.26 5.453 5.453 0 0 0-1.426-.2c-.3 0-.573.028-.819.086a2.1 2.1 0 0 0-.623.242c-.17.104-.3.229-.393.374a.888.888 0 0 0-.14.49c0 .196.053.373.156.529.104.156.252.304.443.444s.423.276.696.41c.273.135.582.274.926.416.47.197.892.407 1.266.628.374.222.695.473.963.753.268.279.472.598.614.957.142.359.214.776.214 1.253 0 .657-.125 1.21-.373 1.656a3.033 3.033 0 0 1-1.012 1.085 4.38 4.38 0 0 1-1.487.596c-.566.12-1.163.18-1.79.18a9.916 9.916 0 0 1-1.84-.164 5.544 5.544 0 0 1-1.512-.493v-2.63a5.033 5.033 0 0 0 3.237 1.2c.333 0 .624-.03.872-.09.249-.06.456-.144.623-.25.166-.108.29-.234.373-.38a1.023 1.023 0 0 0-.074-1.089 2.12 2.12 0 0 0-.537-.5 5.597 5.597 0 0 0-.807-.444 27.72 27.72 0 0 0-1.007-.436c-.918-.383-1.602-.852-2.053-1.405-.45-.553-.676-1.222-.676-2.005 0-.614.123-1.141.369-1.582.246-.441.58-.804 1.004-1.089a4.494 4.494 0 0 1 1.47-.629 7.536 7.536 0 0 1 1.77-.201zm-15.113.188h9.563v2.166H9.506v9.646H6.789v-9.646H3.375z" class="astro-o25vlg2d"></path> </svg>  <span class="file-tree__name astro-o25vlg2d">validate-schema.ts</span>  </span> </li>  </ul> </details>   </li>  </ul> </details>   </li>  </ul> </details>   </li>  </ul> </details>   </li>  </ul> </nav> 
<h3 id="how-claude-sees-skills">How Claude Sees Skills<a class="heading-link" aria-label="Link to section" href="#how-claude-sees-skills"><span class="heading-link-icon">#</span></a></h3>
<p>Claude decides whether to invoke a skill largely based on its <code>description</code>.</p>
<p>You can also ask Claude Code something like:</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="markdown"><code><span class="line"><span style="color:#89DDFF;font-style:italic">&gt;</span><span style="color:#9AA5CE;font-style:italic"> “tell me me exactly how this looks for you </span><span style="color:#BA3C97;font-style:italic">&lt;</span><span style="color:#DE5971;font-style:italic">available_skills</span><span style="color:#BA3C97;font-style:italic">&gt;</span><span style="color:#9AA5CE;font-style:italic"> ?”</span></span></code><button type="button" class="copy" data-code="> “tell me me exactly how this looks for you <available_skills> ?”" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>When it answers, you’ll often see structured blocks that look like <code>&lt;available_skills&gt;</code> (and typically a separate block for slash commands, e.g. <code>&lt;available_commands&gt;</code>).</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="xml"><code><span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#F7768E">available_skills</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">  &lt;</span><span style="color:#F7768E">skill</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;</span><span style="color:#F7768E">name</span><span style="color:#BA3C97">&gt;</span><span style="color:#A9B1D6">dexie-expert</span><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">name</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;</span><span style="color:#F7768E">description</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#A9B1D6">      Dexie.js database guidance. Use when working with</span></span>
<span class="line"><span style="color:#A9B1D6">      IndexedDB, schemas, queries, liveQuery...</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;/</span><span style="color:#F7768E">description</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">  &lt;/</span><span style="color:#F7768E">skill</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">available_skills</span><span style="color:#BA3C97">&gt;</span></span></code><button type="button" class="copy" data-code="<available_skills>
  <skill>
    <name>dexie-expert</name>
    <description>
      Dexie.js database guidance. Use when working with
      IndexedDB, schemas, queries, liveQuery...
    </description>
  </skill>
</available_skills>" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<p>Here’s an abbreviated example of what the <code>&lt;available_skills&gt;</code> section can look like (truncated with <code>...</code>):</p>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="xml"><code><span class="line"><span style="color:#BA3C97">&lt;</span><span style="color:#F7768E">available_skills</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">  &lt;</span><span style="color:#F7768E">skill</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;</span><span style="color:#F7768E">name</span><span style="color:#BA3C97">&gt;</span><span style="color:#A9B1D6">skill-creator</span><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">name</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;</span><span style="color:#F7768E">description</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#A9B1D6">      Guide for creating effective skills. Use when you want to create or update a skill.</span></span>
<span class="line"><span style="color:#A9B1D6">      ...</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;/</span><span style="color:#F7768E">description</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;</span><span style="color:#F7768E">location</span><span style="color:#BA3C97">&gt;</span><span style="color:#A9B1D6">user</span><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">location</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">  &lt;/</span><span style="color:#F7768E">skill</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BA3C97">  &lt;</span><span style="color:#F7768E">skill</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;</span><span style="color:#F7768E">name</span><span style="color:#BA3C97">&gt;</span><span style="color:#A9B1D6">c4-architecture</span><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">name</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;</span><span style="color:#F7768E">description</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#A9B1D6">      Generate architecture documentation using C4 model Mermaid diagrams.</span></span>
<span class="line"><span style="color:#A9B1D6">      ...</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;/</span><span style="color:#F7768E">description</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;</span><span style="color:#F7768E">location</span><span style="color:#BA3C97">&gt;</span><span style="color:#A9B1D6">user</span><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">location</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">  &lt;/</span><span style="color:#F7768E">skill</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#BA3C97">  &lt;</span><span style="color:#F7768E">skill</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;</span><span style="color:#F7768E">name</span><span style="color:#BA3C97">&gt;</span><span style="color:#A9B1D6">vue-composables</span><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">name</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;</span><span style="color:#F7768E">description</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#A9B1D6">      Write high-quality Vue 3 composables following established patterns and best practices.</span></span>
<span class="line"><span style="color:#A9B1D6">      ...</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;/</span><span style="color:#F7768E">description</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">    &lt;</span><span style="color:#F7768E">location</span><span style="color:#BA3C97">&gt;</span><span style="color:#A9B1D6">managed</span><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">location</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"><span style="color:#BA3C97">  &lt;/</span><span style="color:#F7768E">skill</span><span style="color:#BA3C97">&gt;</span></span>
<span class="line"></span>
<span class="line"><span style="color:#A9B1D6">  ...</span></span>
<span class="line"><span style="color:#BA3C97">&lt;/</span><span style="color:#F7768E">available_skills</span><span style="color:#BA3C97">&gt;</span></span></code><button type="button" class="copy" data-code="<available_skills>
  <skill>
    <name>skill-creator</name>
    <description>
      Guide for creating effective skills. Use when you want to create or update a skill.
      ...
    </description>
    <location>user</location>
  </skill>

  <skill>
    <name>c4-architecture</name>
    <description>
      Generate architecture documentation using C4 model Mermaid diagrams.
      ...
    </description>
    <location>user</location>
  </skill>

  <skill>
    <name>vue-composables</name>
    <description>
      Write high-quality Vue 3 composables following established patterns and best practices.
      ...
    </description>
    <location>managed</location>
  </skill>

  ...
</available_skills>" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h3 id="the-dexiejs-solution-3">The Dexie.js Solution<a class="heading-link" aria-label="Link to section" href="#the-dexiejs-solution-3"><span class="heading-link-icon">#</span></a></h3>
<pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="markdown"><code><span class="line"><span style="color:#89DDFF">---</span></span>
<span class="line"><span style="color:#F7768E">name</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> dexie-expert</span></span>
<span class="line"><span style="color:#F7768E">description</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> Dexie.js database guidance. Use when working with IndexedDB, schemas, queries, liveQuery, or database migrations.</span></span>
<span class="line"><span style="color:#F7768E">allowed-tools</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> Read, Grep, Glob, WebFetch</span></span>
<span class="line"><span style="color:#89DDFF">---</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF;font-weight:bold">#</span><span style="color:#89DDFF;font-weight:bold"> Dexie.js Expert</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">When the user needs help with Dexie.js or IndexedDB:</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">1.</span><span style="color:#9AA5CE"> Fetch https://dexie.org/llms.txt</span></span>
<span class="line"><span style="color:#89DDFF">2.</span><span style="color:#9AA5CE"> Fetch only the relevant pages for the task</span></span>
<span class="line"><span style="color:#89DDFF">3.</span><span style="color:#9AA5CE"> Apply the guidance to this repo’s patterns</span></span></code><button type="button" class="copy" data-code="---
name: dexie-expert
description: Dexie.js database guidance. Use when working with IndexedDB, schemas, queries, liveQuery, or database migrations.
allowed-tools: Read, Grep, Glob, WebFetch
---

# Dexie.js Expert

When the user needs help with Dexie.js or IndexedDB:

1. Fetch https://dexie.org/llms.txt
2. Fetch only the relevant pages for the task
3. Apply the guidance to this repo’s patterns" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre>
<h3 id="a-minimal-does-this-even-work-skill">A Minimal “Does This Even Work?” Skill<a class="heading-link" aria-label="Link to section" href="#a-minimal-does-this-even-work-skill"><span class="heading-link-icon">#</span></a></h3>
<p>If you just want to verify that <strong>a Skill can spin up subagents to do work</strong> (via the <code>Task</code> tool), here’s a deliberately dumb smoke test you can copy/paste.</p>
<details class="collapsible astro-kncz7yy6"> <summary class="collapsible-summary astro-kncz7yy6"> <span class="collapsible-icon astro-kncz7yy6"> <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="astro-kncz7yy6"> <polyline points="9 18 15 12 9 6" class="astro-kncz7yy6"></polyline> </svg> </span> SKILL.md (subagent-smoke-test) </summary> <div class="collapsible-content astro-kncz7yy6"> <pre class="astro-code tokyo-night" style="background-color:#1a1b26;color:#a9b1d6;overflow-x:auto;white-space:pre-wrap;word-wrap:break-word" tabindex="0" data-language="markdown"><code><span class="line"><span style="color:#89DDFF">---</span></span>
<span class="line"><span style="color:#F7768E">name</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> subagent-smoke-test</span></span>
<span class="line"><span style="color:#F7768E">description</span><span style="color:#89DDFF">:</span><span style="color:#9ECE6A"> Smoke test for Claude Code subagents. Use when the user wants to verify that spawning a subagent via the Task tool works in this repo.</span></span>
<span class="line"><span style="color:#89DDFF">---</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF;font-weight:bold">#</span><span style="color:#89DDFF;font-weight:bold"> Subagent Smoke Test</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">This skill exists purely to verify that subagents work end-to-end.</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> What to do</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">1.</span><span style="color:#9AA5CE"> Spin up a subagent using the </span><span style="color:#C0CAF5;font-weight:bold">**Task**</span><span style="color:#9AA5CE"> tool.</span></span>
<span class="line"><span style="color:#89DDFF">   -</span><span style="color:#9AA5CE"> Use </span><span style="color:#89DDFF">`subagent_type: general-purpose`</span><span style="color:#9AA5CE">.</span></span>
<span class="line"><span style="color:#89DDFF">   -</span><span style="color:#9AA5CE"> Give it a simple, read-only task:</span></span>
<span class="line"><span style="color:#89DDFF">     -</span><span style="color:#9AA5CE"> Read </span><span style="color:#89DDFF">`package.json`</span><span style="color:#9AA5CE"> and summarize the key scripts.</span></span>
<span class="line"><span style="color:#89DDFF">     -</span><span style="color:#9AA5CE"> Read </span><span style="color:#89DDFF">`astro.config.ts`</span><span style="color:#9AA5CE"> and summarize major integrations.</span></span>
<span class="line"><span style="color:#89DDFF">     -</span><span style="color:#9AA5CE"> Use Glob (or equivalent) to list the top-level folders.</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">2.</span><span style="color:#9AA5CE"> Wait for the subagent to finish.</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">3.</span><span style="color:#9AA5CE"> Return a short report to the user:</span></span>
<span class="line"><span style="color:#89DDFF">   -</span><span style="color:#89DDFF"> `Subagent status: success`</span><span style="color:#9AA5CE"> (or </span><span style="color:#89DDFF">`failed`</span><span style="color:#9AA5CE">)</span></span>
<span class="line"><span style="color:#89DDFF">   -</span><span style="color:#9AA5CE"> A 3–6 bullet summary of what it found</span></span>
<span class="line"><span style="color:#89DDFF">   -</span><span style="color:#9AA5CE"> If it failed, include the most likely fix (e.g. tool permissions, Task tool disabled).</span></span>
<span class="line"></span>
<span class="line"><span style="color:#61BDF2;font-weight:bold">##</span><span style="color:#61BDF2;font-weight:bold"> Suggested Task prompt</span></span>
<span class="line"></span>
<span class="line"><span style="color:#9AA5CE">Use something like this as the Task payload:</span></span>
<span class="line"></span>
<span class="line"><span style="color:#89DDFF">-</span><span style="color:#9AA5CE"> “You are a helper subagent. Do a quick, read-only scan of this repo.</span></span>
<span class="line"><span style="color:#89DDFF">  -</span><span style="color:#9AA5CE"> Read </span><span style="color:#89DDFF">`package.json`</span><span style="color:#9AA5CE"> and summarize the main scripts.</span></span>
<span class="line"><span style="color:#89DDFF">  -</span><span style="color:#9AA5CE"> Read </span><span style="color:#89DDFF">`astro.config.ts`</span><span style="color:#9AA5CE"> and summarize key integrations.</span></span>
<span class="line"><span style="color:#89DDFF">  -</span><span style="color:#9AA5CE"> Glob the repo root and list the top-level folders.</span></span>
<span class="line"><span style="color:#9AA5CE">  Return a concise report.”</span></span></code><button type="button" class="copy" data-code="---
name: subagent-smoke-test
description: Smoke test for Claude Code subagents. Use when the user wants to verify that spawning a subagent via the Task tool works in this repo.
---

# Subagent Smoke Test

This skill exists purely to verify that subagents work end-to-end.

## What to do

1. Spin up a subagent using the **Task** tool.
   - Use `subagent_type: general-purpose`.
   - Give it a simple, read-only task:
     - Read `package.json` and summarize the key scripts.
     - Read `astro.config.ts` and summarize major integrations.
     - Use Glob (or equivalent) to list the top-level folders.

2. Wait for the subagent to finish.

3. Return a short report to the user:
   - `Subagent status: success` (or `failed`)
   - A 3–6 bullet summary of what it found
   - If it failed, include the most likely fix (e.g. tool permissions, Task tool disabled).

## Suggested Task prompt

Use something like this as the Task payload:

- “You are a helper subagent. Do a quick, read-only scan of this repo.
  - Read `package.json` and summarize the main scripts.
  - Read `astro.config.ts` and summarize key integrations.
  - Glob the repo root and list the top-level folders.
  Return a concise report.”" onclick="
            navigator.clipboard.writeText(this.dataset.code);
            this.classList.add('copied');
            setTimeout(() => this.classList.remove('copied'), 3000);
          " aria-label="Copy code"><span class="ready"></span><span class="success"></span></button></pre> </div> </details>  
<h3 id="what-happens-3">What Happens<a class="heading-link" aria-label="Link to section" href="#what-happens-3"><span class="heading-link-icon">#</span></a></h3>
<p>Skills are <strong>auto-discovered</strong> and typically get applied when Claude decides they match the current task. They run <strong>in your main conversation</strong>, so you can iterate live.</p>
<p>If you need a manual, predictable trigger from the terminal, package the workflow as a <strong>slash command</strong> (since <code>/...</code> is for commands).</p>
<h3 id="trade-offs-3">Trade-offs<a class="heading-link" aria-label="Link to section" href="#trade-offs-3"><span class="heading-link-icon">#</span></a></h3>





























<table><thead><tr><th>✅ Pros</th><th>❌ Cons</th></tr></thead><tbody><tr><td data-label="✅ Pros">Auto-discovered based on description</td><td data-label="❌ Cons">Shares main context window space</td></tr><tr><td data-label="✅ Pros">Works in main conversation—live interaction</td><td data-label="❌ Cons">Claude decides when to trigger (may not fire)</td></tr><tr><td data-label="✅ Pros">Can include reference files, scripts, templates</td><td data-label="❌ Cons">More setup than slash commands</td></tr><tr><td data-label="✅ Pros">Deep, reusable workflow packaging</td><td data-label="❌ Cons">Not manually invokable via <code>/...</code> in the terminal</td></tr><tr><td data-label="✅ Pros">Feels like enhanced Claude, not a separate tool</td><td data-label="❌ Cons"></td></tr></tbody></table>
<div class="alert alert-important astro-7kdbuayl"> <p class="alert-title astro-7kdbuayl"> <span class="alert-icon astro-7kdbuayl">📢</span> Key Insight </p> <div class="alert-content astro-7kdbuayl"> <p>In practice, the difference is mostly <strong>UX + packaging</strong>:</p><ul>
<li><strong>Slash commands</strong> are what you can run manually from the terminal via <code>/command</code>.</li>
<li><strong>Skills</strong> are structured, auto-discovered capabilities (often a directory of supporting files) that Claude may apply when relevant.</li>
</ul> </div> </div> 
<hr/>
<h3 id="when-to-use-what">When to use what<a class="heading-link" aria-label="Link to section" href="#when-to-use-what"><span class="heading-link-icon">#</span></a></h3>






























<table><thead><tr><th>Pick this</th><th>When</th><th>Why</th></tr></thead><tbody><tr><td data-label="Pick this"><strong>CLAUDE.md</strong></td><td data-label="When">You want Claude to <em>always</em> start with project rules/context</td><td data-label="Why">Auto-loaded on startup; shared via git</td></tr><tr><td data-label="Pick this"><strong>Slash command</strong></td><td data-label="When">You want an explicit one-shot workflow you run on demand</td><td data-label="Why">Discoverable via <code>/...</code>, can take arguments</td></tr><tr><td data-label="Pick this"><strong>Subagent</strong></td><td data-label="When">The task is research-heavy (lots of reading/searching/synthesis)</td><td data-label="Why">Uses a separate context window; returns a distilled result</td></tr><tr><td data-label="Pick this"><strong>Skill</strong></td><td data-label="When">You want a rich workflow that Claude can auto-apply when it recognizes the task</td><td data-label="Why">Packaged capability (often with supporting files)</td></tr></tbody></table>
<h3 id="how-they-relate">How they relate<a class="heading-link" aria-label="Link to section" href="#how-they-relate"><span class="heading-link-icon">#</span></a></h3>













































<table><thead><tr><th>Mechanism</th><th style="text-align:right">Runs in main conversation</th><th style="text-align:right">Separate context window</th><th style="text-align:right">Can spawn subagents</th><th style="text-align:right">Can use skills</th><th style="text-align:right">Manually runnable via <code>/...</code></th></tr></thead><tbody><tr><td data-label="Mechanism"><strong>CLAUDE.md</strong></td><td data-label="Runs in main conversation" style="text-align:right">✅</td><td data-label="Separate context window" style="text-align:right">❌</td><td data-label="Can spawn subagents" style="text-align:right">❌</td><td data-label="Can use skills" style="text-align:right">❌</td><td data-label="Manually runnable via /..." style="text-align:right">❌</td></tr><tr><td data-label="Mechanism"><strong>Slash command</strong></td><td data-label="Runs in main conversation" style="text-align:right">✅</td><td data-label="Separate context window" style="text-align:right">❌</td><td data-label="Can spawn subagents" style="text-align:right">✅ (by instructing <code>Task</code>)</td><td data-label="Can use skills" style="text-align:right">✅ (indirectly; Claude may apply skills)</td><td data-label="Manually runnable via /..." style="text-align:right">✅</td></tr><tr><td data-label="Mechanism"><strong>Skill</strong></td><td data-label="Runs in main conversation" style="text-align:right">✅</td><td data-label="Separate context window" style="text-align:right">❌</td><td data-label="Can spawn subagents" style="text-align:right">✅ (if <code>Task</code> is allowed)</td><td data-label="Can use skills" style="text-align:right">✅ (Claude may apply multiple skills)</td><td data-label="Manually runnable via /..." style="text-align:right">❌</td></tr><tr><td data-label="Mechanism"><strong>Subagent</strong></td><td data-label="Runs in main conversation" style="text-align:right">❌</td><td data-label="Separate context window" style="text-align:right">✅</td><td data-label="Can spawn subagents" style="text-align:right">⚠️ Possible (depends on allowed tools, e.g. <code>Bash(claude:*)</code>)</td><td data-label="Can use skills" style="text-align:right">✅ (if configured via <code>skills:</code>)</td><td data-label="Manually runnable via /..." style="text-align:right">⚠️ Usually delegated</td></tr></tbody></table>
<h2 id="conclusion">Conclusion<a class="heading-link" aria-label="Link to section" href="#conclusion"><span class="heading-link-icon">#</span></a></h2>
<ul>
<li>Use <strong>subagents</strong> (especially <code>Explore</code> in plan mode) to keep your main context small and focused.</li>
<li>Use <strong>slash commands</strong> when you want an explicit, repeatable terminal entry point.</li>
<li>Use <strong>skills</strong> when you want Claude to auto-apply a richer workflow (often with supporting files).</li>
<li>Use <strong>CLAUDE.md</strong> for short, always-true project conventions and standards.</li>
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
</li> <li class="astro-vj4tpspi">Small tips and trick</li> </ul> </div> <a href="https://alex-op-newsletter.beehiiv.com/subscribe?utm_source=blog&utm_medium=post&utm_campaign=post_claude-code-customization-guide-claudemd-skills-subagents" target="_blank" rel="noopener noreferrer" id="newsletter-subscribe-button" class="inline-flex items-center justify-center gap-2 rounded-full bg-skin-accent px-6 py-3 text-base font-semibold text-skin-inverted shadow-md transition-all duration-200 hover:scale-[1.02] hover:transform hover:opacity-90 astro-vj4tpspi"> <svg class="h-5 w-5 fill-current astro-vj4tpspi" viewBox="0 0 24 24" aria-hidden="true"> <path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z" class="astro-vj4tpspi"></path> </svg>
Subscribe Now
</a> <button id="newsletter-dismiss" data-post-slug="claude-code-customization-guide-claudemd-skills-subagents" class="absolute right-3 top-3 rounded-full p-1 text-skin-base transition-all duration-200 hover:bg-skin-accent hover:bg-opacity-10 hover:text-skin-accent astro-vj4tpspi" aria-label="Close notification"> <svg class="h-5 w-5 astro-vj4tpspi" fill="none" stroke="currentColor" viewBox="0 0 24 24"> <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" class="astro-vj4tpspi"></path> </svg> </button> </div> </div> </div> <ul class="my-8 flex flex-wrap gap-2 astro-vj4tpspi"> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/claude-code/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-2"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">claude-code</span>   </a> </li> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/ai/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-3"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">ai</span>   </a> </li> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/tooling/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-4"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">tooling</span>   </a> </li> <li class="inline-block my-1 astro-blwjyjpt"> <a href="/tags/typescript/" class="
      group
      flex items-center
      rounded-full
      bg-skin-card
      px-3 py-1
      text-skin-base
      hover:bg-skin-accent hover:text-skin-inverted
      text-sm
     astro-blwjyjpt" data-astro-transition-scope="astro-36ssibgs-5"> <svg xmlns="http://www.w3.org/2000/svg" class="mr-1 h-3 w-3 astro-blwjyjpt" viewBox="0 0 20 20" fill="currentColor"> <path fill-rule="evenodd" d="M17.707 9.293a1 1 0 010 1.414l-7 7a1 1 0 01-1.414 0l-7-7A.997.997 0 012 10V5a3 3 0 013-3h5c.256 0 .512.098.707.293l7 7zM5 6a1 1 0 100-2 1 1 0 000 2z" clip-rule="evenodd" class="astro-blwjyjpt"></path> </svg> <span class="astro-blwjyjpt">typescript</span>   </a> </li>  </ul> <div class="flex flex-col-reverse items-center justify-between gap-6 sm:flex-row-reverse sm:items-end sm:gap-4 astro-vj4tpspi"> <button id="back-to-top" class="focus-outline whitespace-nowrap py-1 hover:opacity-75 astro-vj4tpspi"> <svg xmlns="http://www.w3.org/2000/svg" class="rotate-90 astro-vj4tpspi"> <path d="M13.293 6.293 7.586 12l5.707 5.707 1.414-1.414L10.414 12l4.293-4.293z" class="astro-vj4tpspi"></path> </svg> <span class="astro-vj4tpspi">Back to Top</span> </button> <div class="social-icons astro-wkojbtzc"> <span class="italic astro-wkojbtzc">Share this post on:</span> <div class="text-center astro-wkojbtzc"> <a href="https://wa.me/?text=https://alexop.dev/posts/claude-code-customization-guide-claudemd-skills-subagents/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via WhatsApp" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M3 21l1.65 -3.8a9 9 0 1 1 3.4 2.9l-5.05 .9"></path>
      <path d="M9 10a0.5 .5 0 0 0 1 0v-1a0.5 .5 0 0 0 -1 0v1a5 5 0 0 0 5 5h1a0.5 .5 0 0 0 0 -1h-1a0.5 .5 0 0 0 0 1"></path>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post via WhatsApp</span> </a><a href="https://www.facebook.com/sharer.php?u=https://alexop.dev/posts/claude-code-customization-guide-claudemd-skills-subagents/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on Facebook" target="_blank" rel="noopener noreferrer"> <svg
    xmlns="http://www.w3.org/2000/svg"
    class="icon-tabler"
    stroke-linecap="round"
    stroke-linejoin="round"
  >
    <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
    <path
      d="M7 10v4h3v7h4v-7h3l1 -4h-4v-2a1 1 0 0 1 1 -1h3v-4h-3a5 5 0 0 0 -5 5v2h-3"
    ></path>
  </svg> <span class="sr-only astro-wkojbtzc">Share this post on Facebook</span> </a><a href="https://x.com/intent/tweet?url=https://alexop.dev/posts/claude-code-customization-guide-claudemd-skills-subagents/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Tweet this post" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <path d="M22 4.01c-1 .49 -1.98 .689 -3 .99c-1.121 -1.265 -2.783 -1.335 -4.38 -.737s-2.643 2.06 -2.62 3.737v1c-3.245 .083 -6.135 -1.395 -8 -4c0 0 -4.182 7.433 4 11c-1.872 1.247 -3.739 2.088 -6 2c3.308 1.803 6.913 2.423 10.034 1.517c3.58 -1.04 6.522 -3.723 7.651 -7.742a13.84 13.84 0 0 0 .497 -3.753c-.002 -.249 1.51 -2.772 1.818 -4.013z"></path>
    </svg> <span class="sr-only astro-wkojbtzc">Tweet this post</span> </a><a href="https://t.me/share/url?url=https://alexop.dev/posts/claude-code-customization-guide-claudemd-skills-subagents/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via Telegram" target="_blank" rel="noopener noreferrer"> <svg
        xmlns="http://www.w3.org/2000/svg"
        class="icon-tabler"
        stroke-linecap="round"
        stroke-linejoin="round"
      >
        <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
        <path d="M15 10l-4 4l6 6l4 -16l-18 7l4 2l2 6l3 -4"></path>
      </svg> <span class="sr-only astro-wkojbtzc">Share this post via Telegram</span> </a><a href="https://pinterest.com/pin/create/button/?url=https://alexop.dev/posts/claude-code-customization-guide-claudemd-skills-subagents/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on Pinterest" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <line x1="8" y1="20" x2="12" y2="11"></line>
      <path d="M10.7 14c.437 1.263 1.43 2 2.55 2c2.071 0 3.75 -1.554 3.75 -4a5 5 0 1 0 -9.7 1.7"></path>
      <circle cx="12" cy="12" r="9"></circle>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post on Pinterest</span> </a><a href="mailto:?subject=See%20this%20post&#38;body=https://alexop.dev/posts/claude-code-customization-guide-claudemd-skills-subagents/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post via email" target="_blank" rel="noopener noreferrer"> <svg
      xmlns="http://www.w3.org/2000/svg"
      class="icon-tabler"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
      <rect x="3" y="5" width="18" height="14" rx="2"></rect>
      <polyline points="3 7 12 13 21 7"></polyline>
    </svg> <span class="sr-only astro-wkojbtzc">Share this post via email</span> </a><a href="https://www.linkedin.com/shareArticle?mini=true&url=https://alexop.dev/posts/claude-code-customization-guide-claudemd-skills-subagents/" class="group inline-block hover:text-skin-accent link-button astro-wkojbtzc" title="Share this post on LinkedIn" target="_blank" rel="noopener noreferrer"> <svg
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
  </svg> <span class="sr-only astro-wkojbtzc">Share this post on LinkedIn</span> </a> </div> </div>  </div> <section id="comments-section" class="giscus-container"></section> <script type="module">function a(){const e=document.getElementById("comments-section");if(!e)return;e.querySelector(".giscus, iframe")&&(e.innerHTML="");const t=document.createElement("script");t.src="https://giscus.app/client.js",t.setAttribute("data-repo","alexanderop/blog-comments"),t.setAttribute("data-repo-id","R_kgDON-LviQ"),t.setAttribute("data-category","Q&A"),t.setAttribute("data-category-id","DIC_kwDON-Lvic4CnPll"),t.setAttribute("data-mapping","url"),t.setAttribute("data-strict","0"),t.setAttribute("data-reactions-enabled","1"),t.setAttribute("data-emit-metadata","0"),t.setAttribute("data-input-position","bottom"),t.setAttribute("data-theme","dark"),t.setAttribute("data-lang","en"),t.setAttribute("data-loading","lazy"),t.setAttribute("crossorigin","anonymous"),t.async=!0,e.appendChild(t)}a();document.addEventListener("astro:page-load",a);</script>  </main> <footer class="mt-auto astro-sz7xmlte"> <div class="max-w-5xl mx-auto px-4"> <hr class="border-skin-line" aria-hidden="true"> </div> <div class="footer-wrapper astro-sz7xmlte"> <div class="footer-content astro-sz7xmlte"> <div class="copyright-wrapper astro-sz7xmlte"> <span class="astro-sz7xmlte">Copyright &#169; 2026</span> <span class="separator astro-sz7xmlte">&nbsp;|&nbsp;</span> <span class="astro-sz7xmlte">All rights reserved.</span> </div> <div class="rss-prompt astro-sz7xmlte"> <a href="/rss.xml" class="rss-link group astro-sz7xmlte" title="Never miss a post - Subscribe via RSS" onclick="if (window.plausible) window.plausible('RSS Subscribe', { props: { location: 'footer' } })"> <div class="flex items-center gap-2 astro-sz7xmlte"> <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-skin-accent group-hover:animate-pulse astro-sz7xmlte"><path fill="currentColor" d="M19 20.001C19 11.729 12.271 5 4 5v2c7.168 0 13 5.832 13 13.001h2z" class="astro-sz7xmlte"></path><path fill="currentColor" d="M12 20.001h2C14 14.486 9.514 10 4 10v2c4.411 0 8 3.589 8 8.001z" class="astro-sz7xmlte"></path><circle cx="6" cy="18" r="2" fill="currentColor" class="astro-sz7xmlte"></circle> </svg> <span class="text-sm astro-sz7xmlte">Subscribe via RSS</span> </div> </a> </div> <div class="social-icons flex astro-upu6fzxr"> <a href="https://github.com/alexanderop" class="group inline-block hover:text-skin-accent link-button astro-upu6fzxr" title=" alexop.dev on Github" target="_blank" rel="noopener noreferrer"> <svg
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
    </script> </body> </html>  <script>(function(){const postSlug = "claude-code-customization-guide-claudemd-skills-subagents";

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