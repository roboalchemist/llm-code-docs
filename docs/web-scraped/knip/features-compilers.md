# Compilers

Source: https://knip.dev/features/compilers

Projects may have source files that are not JavaScript or TypeScript, and thus
require compilation (or transpilation, or pre-processing, you name it). Files
like.mdx,.astro,.vueand.sveltemay also import other source files
and external dependencies. So ideally, these files are included when linting the
project. That’s why Knip supports compilers.

## Built-in compilers

Knip has built-in “compilers” for the following file extensions:

- .astro
- .css(only enabled bytailwindcss)
- .mdx
- .prisma
- .sass+.scss
- .svelte
- .vue

Knip does not include real compilers for those files, but regular expressions to
collectimportstatements. This is fast, requires no dependencies, and enough
for Knip to build the module graph.

On the other hand, real compilers may expose their own challenges in the context
of Knip. For instance, the Svelte compiler keepsexportsintact, while they
might represent component properties. This results in those exports being
reported as unused by Knip.

The built-in functions seem to do a decent job, but override them however you
like.

Compilers are enabled only if certain dependencies are found. If that’s not
working for your project, settrueand enable any compiler manually:

```typescript
exportdefault{compilers:{mdx:true,},};
```

## Custom compilers

Built-in compilers can be overridden, and additional compilers can be added.
Since compilers are functions, the Knip configuration file must be a dynamic.jsor.tsfile.

### Interface

The compiler function interface is straightforward. Text in, text out:

```typescript
(source:string,filename:string)=>string;
```

This may also be anasyncfunction.

Compilers will automatically have their extension added as a default extension
to Knip. This means you don’t need to add something like**/*.{ts,vue}to theentryorprojectfile patterns manually.

### Examples

- CSS
- MDX
- Svelte
- Vue

#### CSS

Here’s an example, minimal compiler for CSS files:

```typescript
exportdefault{compilers:{css:(text:string)=>[...text.matchAll(/(?<=@)import[^;]+/g)].join('\n'),},};
```

You may wonder why the CSS compiler is not included by default. It’s currently
not clear if it should be included. And if so, what would be the best way to
determine it should be enabled, and what syntax(es) it should support. Note that
Tailwind CSS and SASS/SCSS compilers are included.

#### MDX

Another example, in case the built-in MDX compiler is not enough:

```typescript
import{ compile }from'@mdx-js/mdx';exportdefault{compilers:{mdx:asynctext=>(awaitcompile(text)).toString(),},};
```

#### Svelte

In a Svelte project, the compiler is automatically enabled. Override and use
Svelte’s compiler for better results if the built-in “compiler” is not enough:

```typescript
importtype{ KnipConfig }from'knip';import{ compile }from'svelte/compiler';exportdefault{compilers:{svelte:(source:string)=>compile(source,{}).js.code,},}satisfiesKnipConfig;
```

#### Vue

In a Vue project, the compiler is automatically enabled. Override and use Vue’s
parser for better results if the built-in “compiler” is not enough:

```typescript
importtype{ KnipConfig }from'knip';import{parse,typeSFCScriptBlock,typeSFCStyleBlock,}from'vue/compiler-sfc';functiongetScriptBlockContent(block:SFCScriptBlock|null):string[] {if(!block)return[];if(block.src)return[`import '${block.src}'`];return[block.content];}functiongetStyleBlockContent(block:SFCStyleBlock|null):string[] {if(!block)return[];if(block.src)return[`@import '${block.src}';`];return[block.content];}functiongetStyleImports(content:string):string{return[...content.matchAll(/(?<=@)import[^;]+/g)].join('\n');}constconfig={compilers:{vue:(text:string,filename:string)=>{const{descriptor}=parse(text,{ filename,sourceMap:false});return[...getScriptBlockContent(descriptor.script),...getScriptBlockContent(descriptor.scriptSetup),...descriptor.styles.flatMap(getStyleBlockContent).map(getStyleImports),].join('\n');},},}satisfiesKnipConfig;exportdefaultconfig;
```

ISC License© 2024Lars Kappert

