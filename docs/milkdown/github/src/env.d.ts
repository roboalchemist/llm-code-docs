# Source: https://github.com/Milkdown/milkdown/blob/main/docs/src/env.d.ts

declare module 'builddocs' {
  type BuildOptions = {
    name: string
    filename: string
    main: string
    format: 'markdown'
    templates: string
  }

  function build(options: BuildOptions): string
}
