# Design System Libraries and UI Component Frameworks (2026)

A comprehensive catalog of design system libraries, UI component frameworks, and accessibility-focused solutions for modern web development. This document covers complete design systems, headless UI libraries, and framework-specific component libraries.

**Last Updated**: 2026-01-01
**Research Sources**: Perplexity AI, Tavily Search, GitHub Projects

---

## Table of Contents

1. [Complete Design Systems](#complete-design-systems)
2. [Headless UI Libraries (Unstyled)](#headless-ui-libraries-unstyled)
3. [Tailwind CSS-First Component Libraries](#tailwind-css-first-component-libraries)
4. [React Component Libraries](#react-component-libraries)
5. [Vue Component Libraries](#vue-component-libraries)
6. [Svelte Component Libraries](#svelte-component-libraries)
7. [Angular Component Libraries](#angular-component-libraries)
8. [Enterprise Design Systems](#enterprise-design-systems)
9. [Icon Libraries](#icon-libraries)
10. [Design System Tools & Resources](#design-system-tools--resources)

---

## Complete Design Systems

These provide rich, pre-styled components with comprehensive documentation and design guidelines.

### Material UI (MUI)
- **Description**: Implements Google's Material Design with an extensive component set
- **Best For**: Enterprise applications, modern cross-platform web apps
- **Features**:
  - 50+ pre-built components
  - Advanced data grids and tables
  - Strong theming and customization
  - Full TypeScript support
  - Excellent documentation
- **Frameworks**: React (primary)
- **Licensing**: MIT (open source) and commercial versions
- **Website**: https://mui.com/

### Ant Design (antd)
- **Description**: Enterprise-ready design system with advanced form support and dashboards
- **Best For**: Business applications, admin panels, data-heavy UIs
- **Features**:
  - 50+ components
  - Advanced form handling
  - Data table (Table) component with sorting, filtering, pagination
  - Dashboard templates
  - Multi-language support
  - Figma design kit
- **Frameworks**: React, Angular (ng-zorro), Vue (Ant Design Vue)
- **Licensing**: MIT (open source)
- **Website**: https://ant.design/

### Chakra UI
- **Description**: Developer-friendly design system with intuitive styling and built-in accessibility
- **Best For**: Rapid prototyping, modern web applications, accessibility-first projects
- **Features**:
  - 40+ accessible components
  - Intuitive styling with style props
  - Dark mode support
  - Responsive utilities
  - Excellent developer experience
  - Strong TypeScript support
- **Frameworks**: React
- **Licensing**: MIT (open source)
- **Website**: https://chakra-ui.com/

### Mantine
- **Description**: Feature-rich React component library with 100+ customizable components
- **Best For**: MVPs, rapid development, feature-rich applications
- **Features**:
  - 100+ components
  - Helpful hooks and form utilities
  - Built-in dark mode
  - Responsive design
  - Great documentation
  - Active community
- **Frameworks**: React
- **Licensing**: MIT (open source)
- **Website**: https://mantine.dev/

### PrimeReact
- **Description**: Comprehensive component library with advanced widgets and data visualization
- **Best For**: Enterprise applications, complex dashboards, data-heavy UIs
- **Features**:
  - 100+ components
  - Charts and visualization tools
  - Advanced data tables
  - Themes and templates included
  - Excellent for enterprise use
- **Frameworks**: React
- **Licensing**: MIT (open source) and commercial
- **Website**: https://primereact.org/

### PrimeVue
- **Description**: Rich set of UI components for Vue applications with 90+ components
- **Best For**: Vue applications, enterprise dashboards, comprehensive UI needs
- **Features**:
  - 90+ components
  - 200+ icons included
  - Multiple themes
  - Advanced data visualization
  - Strong Vue 3 support
- **Frameworks**: Vue 3+
- **Licensing**: MIT (open source)
- **Website**: https://primevue.org/

---

## Headless UI Libraries (Unstyled)

Unstyled, logic-focused primitives designed for building custom design systems with maximum control over styling.

### Radix UI
- **Description**: Low-level, unstyled component primitives for building accessible design systems
- **Best For**: Custom design systems, complete styling control, accessibility-first projects
- **Features**:
  - 30+ accessible primitives (Dialog, Tooltip, Select, etc.)
  - Composable architecture
  - Complete keyboard navigation
  - ARIA attributes handled automatically
  - No style opinions - bring your own CSS
  - Excellent documentation
- **Frameworks**: React
- **Licensing**: MIT (open source)
- **Website**: https://www.radix-ui.com/
- **Note**: Foundation for shadcn/ui

### Base UI
- **Description**: Headless component library by MUI team, offering unstyled building blocks
- **Best For**: Custom design systems, teams wanting MUI-level quality without MUI styling
- **Features**:
  - Unstyled, low-level components
  - Some components Radix lacks
  - Strong compatibility with CSS-in-JS and Tailwind
  - Focus on composition
  - Performance-oriented
- **Frameworks**: React
- **Licensing**: MIT (open source)
- **Website**: https://mui.org/base-ui/
- **Note**: Complementary to Radix UI, some prefer certain components from each

### Headless UI
- **Description**: Unstyled, fully accessible UI components designed for Tailwind CSS integration
- **Best For**: Tailwind CSS projects, complete styling control with Tailwind
- **Features**:
  - Unstyled components with complete logic
  - Perfect for Tailwind CSS
  - ARIA compliance built-in
  - Keyboard navigation
  - No visual opinions
  - Great for headless CMS
- **Frameworks**: React, Vue
- **Licensing**: MIT (open source)
- **Website**: https://headlessui.com/

### React Aria
- **Description**: Adobe's accessibility-focused component collection emphasizing keyboard and ARIA handling
- **Best For**: Accessibility-critical applications, teams prioritizing WCAG compliance
- **Features**:
  - Comprehensive accessibility features
  - Keyboard handling library
  - ARIA hooks and utilities
  - Strong keyboard support
  - Great for complex interactions
- **Frameworks**: React
- **Licensing**: MIT (open source)
- **Website**: https://react-spectrum.adobe.com/react-aria/

### Ark UI
- **Description**: Headless UI library with 45+ components designed for building reusable design systems
- **Best For**: Multi-framework projects, design system builders
- **Features**:
  - 45+ components
  - Multi-framework support
  - Fully headless and unstyled
  - Strong accessibility
  - Well-documented primitives
- **Frameworks**: React, Vue, Solid, Svelte
- **Licensing**: MIT (open source)
- **Website**: https://ark-ui.com/

### Reka UI
- **Description**: Vue-first headless component library built for composition
- **Best For**: Vue applications prioritizing accessibility and customization
- **Features**:
  - Headless components for Vue
  - Strong accessibility
  - Fully composable
  - Tailwind CSS friendly
- **Frameworks**: Vue 3+
- **Licensing**: MIT (open source)
- **Website**: https://reka-ui.com/

---

## Tailwind CSS-First Component Libraries

Pre-styled components built specifically for Tailwind CSS, emphasizing code ownership and customization.

### shadcn/ui
- **Description**: Copy-paste component library using Tailwind and Radix primitives, emphasizing code ownership
- **Best For**: Modern Tailwind projects, teams wanting full control over component code
- **Features**:
  - Copy-paste components (not npm packages)
  - Built on Radix UI + Tailwind
  - Full code ownership
  - TypeScript support
  - Dark mode included
  - Easy customization
  - CLI for adding components
- **Frameworks**: React (also shadcn-svelte for Svelte)
- **Licensing**: MIT (open source)
- **Website**: https://ui.shadcn.com/
- **Unique Aspect**: You own the component code, not a dependency

### shadcn-svelte
- **Description**: Svelte port of shadcn/ui, bringing copy-paste components to Svelte
- **Best For**: Svelte projects using Tailwind CSS
- **Features**:
  - Copy-paste Svelte components
  - Radix UI primitives
  - Tailwind CSS styling
  - Full code control
  - SvelteKit integration
- **Frameworks**: Svelte, SvelteKit
- **Licensing**: MIT (open source)
- **Website**: https://www.shadcn-svelte.com/

### Nuxt UI
- **Description**: Comprehensive Vue component library with 125+ accessible, Tailwind CSS components
- **Best For**: Nuxt projects, Vue applications with Tailwind
- **Features**:
  - 125+ production-ready components
  - Built on Reka UI + Tailwind
  - SSR compatible
  - Figma kit included
  - Built by Nuxt team
  - Seamless Nuxt integration
- **Frameworks**: Vue, Nuxt
- **Licensing**: MIT (open source)
- **Website**: https://ui.nuxt.com/

### DaisyUI
- **Description**: Tailwind CSS component library with semantic UI classes and multiple themes
- **Best For**: Quick prototyping, Tailwind projects needing multiple themes
- **Features**:
  - Semantic Tailwind class names
  - Multiple built-in themes
  - 50+ components
  - Dark mode support
  - Small bundle size
  - Easy to customize
- **Frameworks**: Framework-agnostic (works with any JS framework)
- **Licensing**: MIT (open source)
- **Website**: https://daisyui.com/

### Flowbite
- **Description**: Tailwind CSS component library with interactive examples and templates
- **Best For**: Tailwind projects, website builders, quick UI development
- **Features**:
  - 60+ components
  - Interactive examples
  - Figma design system
  - Multiple templates
  - Good documentation
  - Responsive design
- **Frameworks**: Vanilla HTML/CSS, React, Vue, Svelte, Next.js
- **Licensing**: MIT (open source)
- **Website**: https://flowbite.com/

### Flowbite Svelte
- **Description**: Official Svelte port of Flowbite with Tailwind CSS components
- **Best For**: Svelte applications using Tailwind
- **Features**:
  - Svelte-specific components
  - Built on Flowbite design system
  - Tailwind CSS styling
  - SvelteKit ready
  - Interactive components
- **Frameworks**: Svelte, SvelteKit
- **Licensing**: MIT (open source)
- **Website**: https://flowbite-svelte.com/

---

## React Component Libraries

React-specific libraries covering various use cases and philosophies.

### Material-UI (MUI)
*See Complete Design Systems section above*

### Chakra UI
*See Complete Design Systems section above*

### React Admin
- **Description**: Turns REST/GraphQL APIs into admin dashboards with authentication and layouts
- **Best For**: Admin panels, internal tools, rapid dashboard development
- **Features**:
  - REST/GraphQL API integration
  - Built-in authentication
  - Predefined layouts
  - Data providers and hooks
  - Material-UI based
  - Great for CRUD operations
- **Frameworks**: React
- **Licensing**: MIT (open source)
- **Website**: https://marmelab.com/react-admin/

### React Spectrum
- **Description**: Adobe's design system for React with components designed for complex, rich applications
- **Best For**: Enterprise applications, accessibility-critical projects
- **Features**:
  - Comprehensive component set
  - Strong accessibility (WCAG)
  - Dark mode support
  - Customizable theming
  - International support
  - Advanced interactions
- **Frameworks**: React
- **Licensing**: Apache 2.0
- **Website**: https://react-spectrum.adobe.com/react-spectrum/

---

## Vue Component Libraries

Vue-specific solutions with varying levels of styling and customization.

### Vuetify
- **Description**: Material Design implementation for Vue with extensive, production-ready components
- **Best For**: Vue applications wanting Material Design, rapid development
- **Features**:
  - Material Design compliance
  - 50+ components
  - Theming system
  - Dark mode
  - Grid system
  - Icons included
  - Strong documentation
- **Frameworks**: Vue 2, Vue 3
- **Licensing**: MIT (open source)
- **Website**: https://vuetifyjs.com/

### Element Plus
- **Description**: Modern Vue 3 UI library with 80+ components, successor to Element UI
- **Best For**: Vue 3 applications, rapid component-based development
- **Features**:
  - 80+ components
  - Clean, modern design
  - Dark mode
  - Internationalization
  - Form validation
  - Great for dashboards
- **Frameworks**: Vue 3+
- **Licensing**: MIT (open source)
- **Website**: https://element-plus.org/

### Ant Design Vue (antd v)
- **Description**: Vue port of popular React Ant Design library
- **Best For**: Vue applications needing enterprise-grade components
- **Features**:
  - Ant Design components in Vue
  - Enterprise-ready
  - Advanced forms and tables
  - TypeScript support
  - Same design language as React version
- **Frameworks**: Vue 2, Vue 3
- **Licensing**: MIT (open source)
- **Website**: https://www.antdv.com/

### Radix Vue
- **Description**: Vue implementation of Radix UI headless primitives
- **Best For**: Vue projects wanting low-level, accessible components
- **Features**:
  - Radix UI for Vue
  - Fully headless
  - Strong accessibility
  - Composable architecture
  - TypeScript support
- **Frameworks**: Vue 3+
- **Licensing**: MIT (open source)
- **Website**: https://www.radix-vue.com/

### Quasar
- **Description**: Full-featured Vue framework providing components, build tools, and more
- **Best For**: Multi-platform applications (web, mobile, desktop), comprehensive framework needs
- **Features**:
  - 80+ components
  - Framework + components
  - Mobile-first approach
  - Multi-target support (web, mobile, desktop)
  - Built-in tooling
  - Material Design
- **Frameworks**: Vue 2, Vue 3
- **Licensing**: MIT (open source)
- **Website**: https://quasar.dev/

---

## Svelte Component Libraries

Svelte-specific solutions optimized for reactivity and bundle size.

### shadcn-svelte
*See Tailwind CSS-First section above*

### Flowbite Svelte
*See Tailwind CSS-First section above*

### Bits UI
- **Description**: Headless Svelte component library giving developers full control over styling
- **Best For**: Custom design systems, teams wanting maximum customization
- **Features**:
  - Headless/unstyled
  - Full styling control
  - Composable architecture
  - Accessibility-first
  - Tailwind-friendly
- **Frameworks**: Svelte, SvelteKit
- **Licensing**: MIT (open source)
- **Website**: https://www.bitsui.com/

### Melt UI
- **Description**: Headless Svelte component library with focus on composition and customization
- **Best For**: Custom design systems, Svelte applications
- **Features**:
  - Headless components
  - Composable API
  - Tailwind CSS compatible
  - Strong accessibility
  - Zero CSS overhead
- **Frameworks**: Svelte, SvelteKit
- **Licensing**: MIT (open source)
- **Website**: https://melt-ui.com/

### Skeleton
- **Description**: Popular Tailwind CSS UI toolkit for Svelte with component focus
- **Best For**: Svelte applications with Tailwind CSS
- **Features**:
  - Tailwind-based components
  - Responsive design
  - Dark mode
  - Easy customization
  - Great documentation
  - Active community
- **Frameworks**: Svelte, SvelteKit
- **Licensing**: MIT (open source)
- **Website**: https://skeleton.dev/

### Smelte
- **Description**: Svelte-first component library based on Material Design
- **Best For**: Svelte projects wanting Material Design
- **Features**:
  - Material Design components
  - Svelte-optimized
  - Small bundle size
  - Dark mode
  - TypeScript support
- **Frameworks**: Svelte
- **Licensing**: MIT (open source)
- **Website**: https://smeltejs.com/

### Carbon Components Svelte
- **Description**: IBM Carbon design system components for Svelte
- **Best For**: Svelte applications needing enterprise design system
- **Features**:
  - IBM Carbon components
  - Enterprise-grade
  - Accessibility compliance
  - Comprehensive components
- **Frameworks**: Svelte
- **Licensing**: Apache 2.0
- **Website**: https://carbon-components-svelte.onrender.com/

---

## Angular Component Libraries

Angular-specific component solutions for enterprise and rapid development.

### Angular Material
- **Description**: Official Angular design system implementing Material Design
- **Best For**: Angular applications wanting Material Design compliance
- **Features**:
  - 50+ components
  - Material Design
  - Theming system
  - ARIA support
  - Dark mode
  - Built-in animations
  - Official support
- **Frameworks**: Angular 2+
- **Licensing**: MIT (open source)
- **Website**: https://material.angular.io/

### PrimeNG
- **Description**: Comprehensive component library for Angular with 100+ components
- **Best For**: Angular applications needing rich component set
- **Features**:
  - 100+ components
  - Charts and data visualization
  - Advanced data tables
  - Themes and templates
  - Enterprise-grade
  - Strong community
- **Frameworks**: Angular
- **Licensing**: MIT (open source) and commercial
- **Website**: https://primeng.org/

### NG-ZORRO
- **Description**: Enterprise-grade Ant Design for Angular
- **Best For**: Angular applications needing Ant Design components
- **Features**:
  - Ant Design for Angular
  - Enterprise components
  - Advanced forms and tables
  - 60+ components
  - TypeScript support
- **Frameworks**: Angular
- **Licensing**: MIT (open source)
- **Website**: https://ng.ant.design/

### NG Bootstrap
- **Description**: Bootstrap components built for Angular without jQuery dependency
- **Best For**: Angular projects using Bootstrap, familiar Bootstrap patterns
- **Features**:
  - Bootstrap 5 components
  - No jQuery dependency
  - Angular-native
  - Great documentation
  - Community-driven
- **Frameworks**: Angular
- **Licensing**: MIT (open source)
- **Website**: https://ng-bootstrap.github.io/

### NGX Bootstrap
- **Description**: Native Bootstrap components for Angular
- **Best For**: Angular applications needing Bootstrap components
- **Features**:
  - Bootstrap components in Angular
  - No external dependencies
  - TypeScript support
  - Fully responsive
  - Great for Bootstrap migration
- **Frameworks**: Angular
- **Licensing**: MIT (open source)
- **Website**: https://valor-software.com/ngx-bootstrap/

### Clarity Design System
- **Description**: VMware's enterprise design system for Angular with accessibility focus
- **Best For**: Enterprise Angular applications, accessibility-critical projects
- **Features**:
  - Enterprise components
  - Strong accessibility
  - Clarity design language
  - Documentation and UX guidelines
  - Icon library
  - Dark mode
- **Frameworks**: Angular
- **Licensing**: Apache 2.0
- **Website**: https://clarity.design/

### Nebular
- **Description**: Customizable Angular component library built on Eva Design System
- **Best For**: Angular applications wanting customizable components
- **Features**:
  - 40+ components
  - Eva Design System
  - Theme customization
  - Dark mode
  - TypeScript support
  - Great documentation
- **Frameworks**: Angular
- **Licensing**: MIT (open source)
- **Website**: https://akveo.github.io/nebular/

### NG Lightning
- **Description**: Angular component library implementing Salesforce Lightning Design System
- **Best For**: Salesforce development with Angular, Lightning Design System projects
- **Features**:
  - Lightning Design System components
  - Salesforce integration-ready
  - 60+ components
  - Great for Salesforce orgs
- **Frameworks**: Angular
- **Licensing**: MIT (open source)
- **Website**: https://ng-lightning.github.io/ng-lightning/

### Angular Primitives
- **Description**: Low-level headless component library for Angular
- **Best For**: Angular projects building custom design systems
- **Features**:
  - Headless, unstyled components
  - Focus on accessibility
  - Customization and developer experience
  - Composable architecture
- **Frameworks**: Angular
- **Licensing**: MIT (open source)
- **Website**: https://angularprimitives.com/

---

## Enterprise Design Systems

Large-scale, governance-focused design systems used by major organizations.

### IBM Carbon Design System
- **Description**: Scalable, accessible design system for enterprises
- **Best For**: Enterprise applications, organizations needing design governance
- **Features**:
  - Open-source design system
  - Figma variables for unified theming
  - Front-end code kits for React, Angular, Vue
  - UX guidelines and interaction examples
  - Elevation and shadow effects
  - Screen breakpoint variables
  - Responsive design tools
  - Comprehensive documentation
- **Frameworks**: React, Angular, Vue
- **Licensing**: Apache 2.0
- **Website**: https://www.carbondesignsystem.com/

### Microsoft Fluent Design System
- **Description**: Cross-platform design system focused on modern, adaptive UIs
- **Best For**: Microsoft ecosystem applications, cross-platform consistency
- **Features**:
  - Modern, adaptive UI principles
  - Motion and depth focus
  - Cross-platform consistency
  - Enterprise-grade
  - Strong developer handoff
  - Windows and Office integration
- **Frameworks**: React, Web Components, and more
- **Licensing**: Microsoft
- **Website**: https://www.microsoft.com/design/fluent/

### Adobe Spectrum Design System
- **Description**: Accessible, customizable design system with WCAG compliance
- **Best For**: Enterprise applications, accessibility-critical projects
- **Features**:
  - Accessibility-first (WCAG compliance)
  - Customizable design tokens
  - Visual guidelines
  - Component kits
  - Figma kits and XD plugins
  - Inclusive design focus
- **Frameworks**: React (React Spectrum)
- **Licensing**: Apache 2.0
- **Website**: https://spectrum.adobe.com/

### Salesforce Lightning Design System
- **Description**: Enterprise design system for Salesforce applications
- **Best For**: Salesforce development, enterprise CRM applications
- **Features**:
  - Architectural foundation for consistency
  - Comprehensive components for CRM
  - Design tokens
  - Figma library
  - Strong governance
  - Innovation on stable foundation
- **Frameworks**: Web Components, React, Angular (ng-lightning)
- **Licensing**: Creative Commons
- **Website**: https://www.lightningdesignsystem.com/

### Atlassian Design System
- **Description**: Design system ensuring consistency across Atlassian product suite (Jira, Confluence, etc.)
- **Best For**: Large product ecosystems, design consistency at scale
- **Features**:
  - Design tokens
  - Component library
  - Design guidelines
  - Figma integration
  - Multi-product consistency
- **Frameworks**: React
- **Licensing**: Atlassian
- **Website**: https://atlassian.design/

---

## Icon Libraries

Curated collections of SVG icons used with component libraries.

### Lucide Icons
- **Description**: Beautiful, consistent icon library available as React components
- **Best For**: Modern applications, consistent icon usage
- **Features**:
  - 400+ icons
  - SVG format
  - React components
  - Figma file
  - Consistent design
  - Regularly updated
- **Frameworks**: React, Svelte, Vue, Web Components
- **Licensing**: ISC (open source)
- **Website**: https://lucide.dev/

### Radix Icons
- **Description**: A crisp set of 15x15 icons designed for use in interfaces
- **Best For**: UI component libraries, clean icon aesthetics
- **Features**:
  - Curated icon set
  - Consistent sizing (15x15)
  - Clean, minimal design
  - SVG-based
  - React components
- **Frameworks**: React
- **Licensing**: MIT (open source)
- **Website**: https://radix-ui.com/icons

### Phosphor Icons
- **Description**: Flexible icon library designed with multiple weights and styles
- **Best For**: Applications wanting flexible icon styling
- **Features**:
  - 6 icon weights
  - 800+ icons
  - Multiple styles
  - Web font and React components
  - Consistent design language
- **Frameworks**: React, Vue, Svelte
- **Licensing**: MIT (open source)
- **Website**: https://phosphoricons.com/

### Heroicons
- **Description**: Beautiful hand-crafted SVG icons by Tailwind Labs
- **Best For**: Tailwind CSS projects, clean icon aesthetics
- **Features**:
  - Hand-crafted quality
  - Tailwind CSS optimized
  - React and Vue components
  - Consistent design
  - Well-maintained
- **Frameworks**: React, Vue, Solid
- **Licensing**: MIT (open source)
- **Website**: https://heroicons.com/

### Font Awesome
- **Description**: Popular icon library with vast icon collection
- **Best For**: Projects needing comprehensive icon coverage
- **Features**:
  - 2000+ icons
  - Font and SVG options
  - Pro and free versions
  - Multiple frameworks support
  - Well-established
- **Frameworks**: Universal (web, React, Vue, Angular)
- **Licensing**: CC BY 4.0 (free), commercial (pro)
- **Website**: https://fontawesome.com/

---

## Design System Tools & Resources

Tools and platforms for managing, documenting, and scaling design systems.

### Storybook
- **Description**: Development environment for building and documenting UI components
- **Best For**: Component documentation, visual testing, design systems management
- **Features**:
  - Interactive component development
  - Automatic documentation generation
  - Multiple add-ons for testing
  - UI snapshots
  - Component discovery
  - Great for collaboration
- **Website**: https://storybook.js.org/

### Figma
- **Description**: Design and prototyping tool with component systems and developer handoff
- **Best For**: Design-to-development workflow, component libraries
- **Features**:
  - Design tokens management
  - Component libraries
  - Developer inspection
  - Design system versioning
  - Cross-team collaboration
- **Website**: https://www.figma.com/

### Zeroheight
- **Description**: Platform for managing design system documentation and component libraries
- **Best For**: Design system documentation, team collaboration
- **Features**:
  - Design system documentation
  - Component documentation
  - Design tokens management
  - Multi-workspace support
  - Figma integration
- **Website**: https://www.zeroheight.com/

### Supernova
- **Description**: Design system management and code generation platform
- **Best For**: Scaling design systems, documentation automation
- **Features**:
  - Design system management
  - Code generation
  - Design tokens
  - Documentation automation
  - Multi-framework support
- **Website**: https://www.supernova.io/

### Chromatic
- **Description**: Visual testing and documentation platform built on Storybook
- **Best For**: Component visual testing, design system quality assurance
- **Features**:
  - Visual regression testing
  - Component snapshots
  - Automated testing
  - CI/CD integration
  - Collaboration features
- **Website**: https://www.chromatic.com/

---

## Selection Guide

### For React Applications
- **Complete Design**: Material-UI, Chakra UI, Mantine
- **Headless**: Radix UI, Base UI, React Aria
- **Tailwind-First**: shadcn/ui, Headless UI, DaisyUI
- **Enterprise**: IBM Carbon, Adobe Spectrum, MUI

### For Vue Applications
- **Complete Design**: Vuetify, Element Plus, Ant Design Vue
- **Modern & Tailwind**: Nuxt UI
- **Headless**: Radix Vue, Reka UI
- **Enterprise**: PrimeVue, Quasar

### For Svelte Applications
- **Tailwind-First**: shadcn-svelte, Skeleton, Flowbite Svelte
- **Headless**: Bits UI, Melt UI
- **Material Design**: Smelte, Carbon Components Svelte

### For Angular Applications
- **Official**: Angular Material
- **Enterprise**: NG-ZORRO, PrimeNG, Clarity
- **Bootstrap-based**: NG Bootstrap, NGX Bootstrap

### For Accessibility & Compliance
- **Priority One**: React Aria, Radix UI, Base UI, headless libraries
- **Enterprise Grade**: IBM Carbon, Adobe Spectrum, Clarity Design System
- **Testing-Friendly**: Storybook with accessibility add-ons

### For Speed & Prototyping
- **Fastest**: DaisyUI, Mantine, PrimeReact
- **Tailwind-Based**: shadcn/ui (full control), Nuxt UI (comprehensive)
- **Copy-Paste**: shadcn/ui, shadcn-svelte

### For Enterprise/Large Teams
- **Governance & Scale**: IBM Carbon, Microsoft Fluent, Salesforce Lightning
- **Design Tokens**: Supernova, Zeroheight for management
- **Multi-Framework**: Ark UI, Ant Design

---

## Key Trends (2026)

1. **Headless-First Approach**: Companies increasingly choosing unstyled primitives (Radix UI, Base UI, React Aria) to maintain design control
2. **Copy-Paste Pattern**: shadcn/ui model gaining popularity for full code ownership
3. **Design Tokens**: Enterprise systems focusing on tokenized design for consistency
4. **Accessibility First**: WCAG compliance becoming standard, not optional
5. **Multi-Framework Support**: Libraries supporting React, Vue, Svelte, Angular (e.g., Ark UI, Reka UI)
6. **Tailwind CSS Integration**: Tailwind-first libraries becoming default for new projects
7. **Figma Integration**: Design-to-code workflows improving across platforms
8. **Dark Mode Standard**: All modern libraries including dark mode support

---

## Research Sources

- Perplexity AI research (2026-01-01)
- Tavily Search results
- Official project documentation
- GitHub repositories and discussions
- Community feedback from Reddit, Dev.to, and blogs

---

## License

This document is provided as a comprehensive reference for design system and UI component framework selection. Individual libraries maintain their own licenses as noted (mostly MIT and Apache 2.0 for open-source projects).
