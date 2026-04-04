# Source: https://logo-soup.sanity.dev/docs/introduction.md

> ## Documentation Index
> Fetch the complete documentation index at: https://logo-soup.sanity.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Introduction

> A tiny framework-agnostic library that makes logos look good together.

export const FrameworkGrid = () => {
  const svgl = "https://raw.githubusercontent.com/pheralb/svgl/main/static/library";
  const frameworks = [{
    name: "React",
    logo: `${svgl}/react_dark.svg`,
    href: "/frameworks/react",
    desc: "Component + hook"
  }, {
    name: "Vue",
    logo: `${svgl}/vue.svg`,
    href: "/frameworks/vue",
    desc: "Composable"
  }, {
    name: "Svelte",
    logo: `${svgl}/svelte.svg`,
    href: "/frameworks/svelte",
    desc: "Runes-compatible store"
  }, {
    name: "Solid",
    logo: `${svgl}/solidjs.svg`,
    href: "/frameworks/solid",
    desc: "Reactive primitive"
  }, {
    name: "Angular",
    logo: `${svgl}/angular.svg`,
    href: "/frameworks/angular",
    desc: "Injectable service"
  }, {
    name: "jQuery",
    logo: `${svgl}/jquery.svg`,
    href: "/frameworks/jquery",
    desc: "$.fn plugin"
  }, {
    name: "Vanilla JS",
    logo: `${svgl}/javascript.svg`,
    href: "/frameworks/vanilla",
    desc: "Core engine directly"
  }, {
    name: "Your framework",
    logo: null,
    href: "/frameworks/custom",
    desc: "Build your own adapter"
  }];
  return <div className="not-prose grid grid-cols-2 sm:grid-cols-4 gap-3 my-6">
      {frameworks.map(fw => <a key={fw.name} href={fw.href} className="group flex flex-col items-center gap-2.5 rounded-xl border border-zinc-200 dark:border-zinc-700 bg-white dark:bg-zinc-900 px-4 py-5 transition-colors hover:border-zinc-400 dark:hover:border-zinc-500 no-underline">
          {fw.logo ? <img src={fw.logo} alt={fw.name} className="h-8 w-8" draggable={false} /> : <span className="flex items-center justify-center h-8 w-8 rounded-md bg-zinc-100 dark:bg-zinc-800 text-zinc-400 dark:text-zinc-500 text-lg">
              +
            </span>}
          <div className="text-center">
            <div className="text-sm font-medium text-zinc-900 dark:text-zinc-100">
              {fw.name}
            </div>
            <div className="text-xs text-zinc-500 dark:text-zinc-400">
              {fw.desc}
            </div>
          </div>
        </a>)}
    </div>;
};

export const LogoSoupDemo = () => {
  const data = [["coda", 247, 82, 77, 26, -2.5], ["reforge", 420, 100, 112, 23, 0.5], ["kahoot", 294, 100, 82, 28, -1.0], ["cursor", 300, 71, 103, 24, -0.3], ["wetransfer", 371, 55, 116, 17, -0.9], ["redis", 170, 54, 78, 25, -2.1], ["expedia", 300, 67, 108, 22, -0.1], ["browser-comp", 274, 190, 78, 54, -1.4], ["hinge", 332, 126, 79, 30, 1.0], ["too-good-to-go", 250, 200, 64, 52, -1.4], ["unity", 305, 112, 80, 29, 0], ["keystone", 400, 80, 113, 23, 1.9], ["retool", 321, 63, 107, 21, -0.4], ["loveholidays", 357, 58, 130, 21, -1.5], ["rad-power-bikes", 427, 33, 164, 13, 0.6], ["stereolabs", 372, 50, 131, 18, -1.5], ["pinecone", 434, 90, 118, 24, -3.0], ["clerk", 317, 92, 89, 26, -1.1], ["samsung", 325, 50, 110, 17, 0], ["customer.io", 400, 54, 129, 18, -0.2]];
  const base = "https://raw.githubusercontent.com/sanity-labs/logo-soup/main/static/logos";
  const uniformH = 28;
  const displayScale = 0.8;
  const [on, setOn] = useState(true);
  const [count, setCount] = useState(12);
  return <div className="not-prose">
      <div className="rounded-xl border border-zinc-200 dark:border-zinc-700 overflow-hidden bg-white dark:bg-zinc-900">
        <div className="flex items-center justify-center gap-7 flex-wrap px-6 py-8 min-h-[100px]">
          {data.slice(0, count).map(([name, nw, nh, dw, dh, ty]) => <img key={name} src={`${base}/${name}.svg`} alt={name} draggable={false} className="dark:invert" style={{
    width: on ? `${dw * displayScale}px` : `${nw / nh * uniformH}px`,
    height: on ? `${dh * displayScale}px` : `${uniformH}px`,
    objectFit: "contain",
    transform: on && ty ? `translateY(${ty * displayScale}px)` : "none",
    transition: "all 0.4s cubic-bezier(0.4, 0, 0.2, 1)"
  }} />)}
        </div>

        <div className="border-t border-zinc-200 dark:border-zinc-700 px-5 py-3.5 flex items-center justify-between gap-4">
          <div className="flex items-center gap-2.5">
            <button type="button" onClick={() => setOn(!on)} className={`relative inline-flex h-5 w-9 shrink-0 items-center rounded-full transition-colors ${on ? "bg-[#f36458]" : "bg-zinc-300 dark:bg-zinc-600"}`} role="switch" aria-checked={on} aria-label="Toggle Logo Soup">
              <span className={`inline-block h-3.5 w-3.5 rounded-full bg-white shadow-sm transition-transform ${on ? "translate-x-[18px]" : "translate-x-[3px]"}`} />
            </button>
            <span className="text-xs font-medium text-zinc-500 dark:text-zinc-400">
              Logo Soup {on ? "on" : "off"}
            </span>
          </div>

          <label className="flex items-center gap-2.5">
            <span className="text-xs font-medium text-zinc-500 dark:text-zinc-400">
              Logos
            </span>
            <input type="range" min={3} max={data.length} step={1} value={count} onChange={e => setCount(Number(e.target.value))} className="w-24 h-1.5 rounded-full appearance-none cursor-pointer" style={{
    background: `linear-gradient(to right, #f36458 ${(count - 3) / (data.length - 3) * 100}%, #e5e7eb ${(count - 3) / (data.length - 3) * 100}%)`
  }} />
            <span className="text-xs tabular-nums font-medium text-zinc-500 dark:text-zinc-400 w-5 text-right">
              {count}
            </span>
          </label>
        </div>
      </div>
      <p className="text-sm text-zinc-500 dark:text-zinc-400 mt-3 text-center">
        Real values from <code className="text-xs">createLogoSoup()</code>
        {" · "}
        <a href="https://logo-soup.sanity.dev/?path=/story/logosoup--default" className="text-[#f36458] hover:underline" target="_blank" rel="noopener noreferrer">
          Open playground →
        </a>
      </p>
    </div>;
};

# 🍜 Logo Soup

Real-world logos are messy. Some have padding, some don't. Some are dense and blocky, others are thin and airy. Put them in a row and they look chaotic. Logo Soup fixes this automatically.

<LogoSoupDemo />

## What it does

Logo Soup analyzes each logo image on a `<canvas>` and normalizes them so they appear visually balanced when displayed together. No server, no AI, fully deterministic.

1. **Content Detection** — Finds the true boundaries of each logo, ignoring whitespace and padding baked into the image
2. **Aspect Ratio Normalization** — Balances wide and tall logos so neither dominates
3. **Density Compensation** — Measures visual weight so dense/bold logos don't overpower light/thin ones
4. **Irradiation Compensation** — Adjusts for the optical illusion where light content on dark backgrounds appears larger

<CardGroup cols={2}>
  <Card title="Read the deep-dive" icon="newspaper" href="https://www.sanity.io/blog/the-logo-soup-problem">
    The full story behind the problem and the math behind the solution.
  </Card>

  <Card title="Try the playground" icon="play" href="https://logo-soup.sanity.dev">
    Interactive Storybook with real logos and tunable parameters.
  </Card>
</CardGroup>

## Framework support

Logo Soup is a single npm package with subpath exports for every major framework:

<FrameworkGrid />

## Architecture

The library is built around a framework-agnostic core engine (`createLogoSoup`) that handles all image loading, measurement, normalization, caching, and cancellation. Each framework adapter is a thin wrapper (30–80 lines) that bridges the engine's `subscribe`/`getSnapshot` interface into the framework's reactivity model.

```
@sanity-labs/logo-soup          → Core engine, types, utilities
@sanity-labs/logo-soup/react    → useLogoSoup hook + LogoSoup component
@sanity-labs/logo-soup/vue      → useLogoSoup composable
@sanity-labs/logo-soup/svelte   → createLogoSoup (runes-compatible)
@sanity-labs/logo-soup/solid    → useLogoSoup primitive
@sanity-labs/logo-soup/angular  → LogoSoupService (Injectable)
@sanity-labs/logo-soup/node     → measureImage / measureImages (server-side)
```

Tree-shaking ensures a React consumer never pulls in Vue/Svelte/Solid/Angular code, and vice versa. The [Node.js adapter](/frameworks/node) lets you pre-compute measurements at build time or in API routes, so clients skip all canvas work. Need a framework we don't support? [Build your own adapter](/frameworks/custom) in 20–40 lines.


Built with [Mintlify](https://mintlify.com).