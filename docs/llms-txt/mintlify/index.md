# Source: https://mintlify.com/docs/index.md

# Source: https://mintlify.com/docs/guides/index.md

# Source: https://mintlify.com/docs/editor/index.md

# Source: https://mintlify.com/docs/components/index.md

# Source: https://mintlify.com/docs/index.md

# Source: https://mintlify.com/docs/guides/index.md

# Source: https://mintlify.com/docs/editor/index.md

# Source: https://mintlify.com/docs/components/index.md

# Source: https://mintlify.com/docs/index.md

# Introduction

> Meet the next generation of documentation. AI-native, beautiful out-of-the-box, and built for developers.

export const HeroCard = ({filename, title, description, href}) => {
  return <a className="group cursor-pointer pb-8" href={href}>
      <img src={`https://mintlify.s3.us-west-1.amazonaws.com/mintlify/images/hero/${filename}.png`} className="block dark:hidden pointer-events-none group-hover:scale-105 transition-all duration-100" />
      <img src={`https://mintlify.s3.us-west-1.amazonaws.com/mintlify/images/hero/${filename}-dark.png`} className="pointer-events-none group-hover:scale-105 transition-all duration-100 hidden dark:block" />
      <h3 className="mt-5 text-gray-900 dark:text-zinc-50 font-medium">
        {title}
      </h3>
      <span className="mt-1.5">{description}</span>
    </a>;
};


<div className="relative">
  <div className="absolute top-0 left-0 right-0">
    <img src="https://mintcdn.com/mintlify/XV_SyGkZAfstDtOP/images/hero/background-light.png?fit=max&auto=format&n=XV_SyGkZAfstDtOP&q=85&s=82cf18f9db68a6bbd99c38964acafd86" className="block dark:hidden pointer-events-none" alt="Decorative background image." data-og-width="2304" width="2304" data-og-height="682" height="682" data-path="images/hero/background-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/XV_SyGkZAfstDtOP/images/hero/background-light.png?w=280&fit=max&auto=format&n=XV_SyGkZAfstDtOP&q=85&s=ef698866e70d4b74299e21694c171a63 280w, https://mintcdn.com/mintlify/XV_SyGkZAfstDtOP/images/hero/background-light.png?w=560&fit=max&auto=format&n=XV_SyGkZAfstDtOP&q=85&s=157a310f604bad6049aac3c19fed5b50 560w, https://mintcdn.com/mintlify/XV_SyGkZAfstDtOP/images/hero/background-light.png?w=840&fit=max&auto=format&n=XV_SyGkZAfstDtOP&q=85&s=df2b30333ebe622981ad85a922e32c8b 840w, https://mintcdn.com/mintlify/XV_SyGkZAfstDtOP/images/hero/background-light.png?w=1100&fit=max&auto=format&n=XV_SyGkZAfstDtOP&q=85&s=efa193f129abe90d070c7a8a5740e0dd 1100w, https://mintcdn.com/mintlify/XV_SyGkZAfstDtOP/images/hero/background-light.png?w=1650&fit=max&auto=format&n=XV_SyGkZAfstDtOP&q=85&s=4ff2f60e32f25b666910b7a033654d90 1650w, https://mintcdn.com/mintlify/XV_SyGkZAfstDtOP/images/hero/background-light.png?w=2500&fit=max&auto=format&n=XV_SyGkZAfstDtOP&q=85&s=e55741f00a5b8d5e2bbb93368da658e8 2500w" />

    <img src="https://mintcdn.com/mintlify/XV_SyGkZAfstDtOP/images/hero/background-dark.png?fit=max&auto=format&n=XV_SyGkZAfstDtOP&q=85&s=6f10314274fa914f283a7dcf72ce0e49" className="hidden dark:block pointer-events-none" alt="Decorative background image." data-og-width="2304" width="2304" data-og-height="682" height="682" data-path="images/hero/background-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/XV_SyGkZAfstDtOP/images/hero/background-dark.png?w=280&fit=max&auto=format&n=XV_SyGkZAfstDtOP&q=85&s=6acf978ad21e1f178f77017c99be308b 280w, https://mintcdn.com/mintlify/XV_SyGkZAfstDtOP/images/hero/background-dark.png?w=560&fit=max&auto=format&n=XV_SyGkZAfstDtOP&q=85&s=eb1549c355b7bc8c0282c284d0f5cb09 560w, https://mintcdn.com/mintlify/XV_SyGkZAfstDtOP/images/hero/background-dark.png?w=840&fit=max&auto=format&n=XV_SyGkZAfstDtOP&q=85&s=10b26bada91c5fc3fbe221cf764099c9 840w, https://mintcdn.com/mintlify/XV_SyGkZAfstDtOP/images/hero/background-dark.png?w=1100&fit=max&auto=format&n=XV_SyGkZAfstDtOP&q=85&s=2a13e59d93ce3eae401d2d6a6f008070 1100w, https://mintcdn.com/mintlify/XV_SyGkZAfstDtOP/images/hero/background-dark.png?w=1650&fit=max&auto=format&n=XV_SyGkZAfstDtOP&q=85&s=da7d0af10de69bbea14cde7cb5a310c8 1650w, https://mintcdn.com/mintlify/XV_SyGkZAfstDtOP/images/hero/background-dark.png?w=2500&fit=max&auto=format&n=XV_SyGkZAfstDtOP&q=85&s=3c09eabb789e005086fcb80b6d223958 2500w" />
  </div>

  <div className="relative z-10 px-4 py-16 lg:py-48 lg:pb-24 max-w-3xl mx-auto">
    <h1 className="block text-4xl font-medium text-center text-gray-900 dark:text-zinc-50 tracking-tight">
      Documentation
    </h1>

    <div className="max-w-xl mx-auto px-4 mt-4 text-lg text-center text-gray-500 dark:text-zinc-500">
      Meet the next generation of documentation. AI-native, beautiful out-of-the-box, and built for developers and teams.
    </div>

    <div className="px-6 lg:px-0 mt-12 lg:mt-24 grid sm:grid-cols-2 gap-x-6 gap-y-4">
      <HeroCard filename="rocket" title="Quickstart" description="Deploy your first docs site in minutes with our step-by-step guide" href="/quickstart" />

      <HeroCard filename="cli" title="CLI installation" description="Install the CLI to preview and develop your docs locally" href="/installation" />

      <HeroCard filename="editor" title="Web editor" description="Make quick updates and manage content with our browser-based editor" href="/editor" />

      <HeroCard filename="components" title="Components" description="Build rich, interactive documentation with our ready-to-use components" href="/text" />
    </div>
  </div>
</div>
