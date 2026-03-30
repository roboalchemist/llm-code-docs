# Source: https://kuma-ui.com/docs

Title: Kuma UI

URL Source: https://kuma-ui.com/docs

Published Time: Tue, 10 Mar 2026 03:55:31 GMT

Markdown Content:
Overview
--------

Why Kuma UI?[](https://kuma-ui.com/docs#why-kuma-ui)
----------------------------------------------------

### From Runtime CSS-in-JS to Zero-Runtime CSS-in-JS[](https://kuma-ui.com/docs#from-runtime-css-in-js-to-zero-runtime-css-in-js)

Initially, runtime CSS-in-JS allowed developers to express CSS entirely in JavaScript. It was powerful, but the need to inject styles into the DOM at runtime led to performance issues. Moreover, these libraries were incompatible with React Server Components (RSC).

Zero-runtime CSS-in-JS emerged as a solution to this challenge. It statically analyzes CSS written in JS during the build process, thereby extracting CSS ahead of time and overcoming the performance issues of runtime CSS-in-JS.

However, zero-runtime CSS-in-JS had its drawbacks. Since CSS was extracted statically at build time, it became impossible to make dynamic style changes—something easily achieved with runtime CSS-in-JS. This restricted JavaScript's expressive power.

### The Hybrid Approach[](https://kuma-ui.com/docs#the-hybrid-approach)

Enter Kuma UI, adopting a **Hybrid approach**. Our solution is to statically extract styles that can be determined at build time and to perform a static "dirty check" on styles that may change dynamically, injecting them at runtime.

This way, Kuma UI brings together **the performance benefits of zero-runtime CSS-in-JS and the expressive power of runtime CSS-in-JS**.

With Kuma UI, you can harness the full power of JavaScript for styling without compromising on performance or compatibility with modern technologies like RSC.

### Headless UI Components[](https://kuma-ui.com/docs#headless-ui-components)

Kuma UI is a headless component library. This means that every component in the library is unstyled, providing the utmost flexibility for users to apply their own styles. This doesn't mean you're left alone to grapple with styles. **Kuma UI is equipped with a powerful theming capability**, allowing you to combine your own design tokens as you please. Here's how you can write your components with Kuma UI:

### Familiar Developer Experience[](https://kuma-ui.com/docs#familiar-developer-experience)

At Kuma UI, we're passionate about providing a familiar and intuitive developer experience. If you've used [Chakra UI (opens in a new tab)](https://chakra-ui.com/), [Styled System (opens in a new tab)](https://styled-system.com/), or [Native Base (opens in a new tab)](https://nativebase.io/), you'll feel right at home with Kuma UI. However, the benefit with Kuma UI is that while you're in familiar territory, you get to enjoy superior performance, greater flexibility, and a system that adapts to the evolving needs of modern web development.

Inspirations[](https://kuma-ui.com/docs#inspirations)
-----------------------------------------------------

Kuma UI is standing on the shoulders of giants. We've drawn inspiration from some of the most innovative libraries in the CSS-in-JS ecosystem.

* **[Styled System (opens in a new tab)](https://styled-system.com/):** The concept of system props in Kuma UI is heavily inspired by Styled System.

* **[Chakra UI (opens in a new tab)](https://chakra-ui.com/):** From Chakra UI, we've learned the power of simplicity and intuitive API design.

* **[Native Base (opens in a new tab)](https://nativebase.io/):** Native Base's philosophy of a completely customizable and themeable library aligns with our own.

* **[Panda CSS (opens in a new tab)](https://panda-css.com/):** The simplicity and directness of Panda CSS have influenced our approach to Hybrid CSS-in-JS.

* **[Linaria (opens in a new tab)](https://github.com/callstack/linaria):** The static extraction concept in Kuma UI is inspired by Linaria.

* **[Vanilla Extract (opens in a new tab)](https://vanilla-extract.style/):** From Vanilla Extract, we learned about the possibility of theming and zero-runtime CSS in TypeScript.

Each of these libraries brought something unique to the table, and we've incorporated their best features into Kuma UI. It's our way of saying "thank you" to these incredible open-source projects, and our way of giving back to the community.

What's Next?[](https://kuma-ui.com/docs#whats-next)
---------------------------------------------------

Now that you have a sense of what Kuma UI is all about, dive into the documentation to explore in detail. You can start by learning about our [theming system](https://www.kuma-ui.com/docs/Theme/CustomizingTheme), or jump straight into our [component docs](https://www.kuma-ui.com/docs/Components/Box).

Welcome to Kuma UI. We can't wait to see what you build with it 🐻‍❄️

Last updated on August 31, 2024

[Installation](https://www.kuma-ui.com/docs/install "Installation")
