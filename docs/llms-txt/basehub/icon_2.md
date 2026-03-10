# Icon

> Provides seamless rendering of SVG elements in your application.

## Overview

The Icon block is a primitive block type that allows you to store and render SVG icons directly in your applications as React components. Unlike traditional image blocks that you’ll need to render via `<img />` elements, Icon blocks output as SVG which you can render as a DOM element, providing full access to vector properties for styling, animations, and dynamic theming.

## Key Benefits

*   **Dynamic Color Customization**: Change icon colors programmatically, perfect for theme switching between dark and light modes
    
*   **SVG Animation Support**: Access to all SVG elements (paths, rects, circles) enables complex animations and interactions
    
*   **Streamlined Workflow**: No need to download, optimize, and upload SVG files—paste or upload directly in the BaseHub dashboard
    
*   **Better Preview**: Enhanced preview functionality in the dashboard with zoom capabilities for detailed inspection
    

## Installation

Make sure you have the latest version of BaseHub installed to access the Icon component:

```
pnpm add basehub@latest
```

## Basic Usage

Import the `Icon` component from `basehub/react-svg` and use it to render icon blocks:

```
import { Icon } from 'basehub/react-icon'
import { Pump } from 'basehub/react-pump'

export const SocialLinks = () => {
  return (
    <Pump
      queries={[
        {
          socialLinks: {
            items: { _id: true, icon: true, label: true, href: true },
          },
        },
      ]}
    >
      {async ([{ socialLinks }]) => {
        'use server'

        return socialLinks.items.map((link) => {
          return (
            <a
              key={link._id}
              href={link.href}
              target="_blank"
              rel="noopener noreferrer"
            >
              <Icon content={link.icon} />
              <span>{link.label}</span>{' '}
            </a>
          )
        })
      }}
    </Pump>
  )
}
```

## Advanced Customization

You can customize individual SVG elements within the icon. This allows for styling and animations:

```

import { Icon } from 'basehub/react-icon'

export const AnimatedIcon = ({ iconContent }: { iconContent: string }) => {
  return (
    <Icon
      content={iconContent}
      components={{
        svg: (props) => <svg {...props} style={{ width: 48, height: 48 }} />,
        path: (props) => (
          <path
            {...props}
            style={{ fill: 'currentColor', transition: 'all 0.3s ease' }}
            className="hover:fill-blue-500 animate-pulse"
          />
        ),
        circle: (props) => (
          <circle
            {...props}
            style={{
              stroke: 'currentColor',
              strokeDasharray: '10,5',
              animation: 'dash 2s linear infinite',
            }}
          />
        ),
      }}
    />
  )
}
```

## GraphQL Schema

In your GraphQL queries, Icon blocks are returned as strings containing the SVG content:

```
{
  socialLinks {
    items {
      _id
      icon  # string containing SVG markup
      label
      href
  }
}
```

## Constraints

Icon blocks support the following configuration options:

\[data-radix-scroll-area-viewport\]{scrollbar-width:none;-ms-overflow-style:none;-webkit-overflow-scrolling:touch;}\[data-radix-scroll-area-viewport\]::-webkit-scrollbar{display:none}

Property

Description

Is required

Makes the icon field mandatory. When true, the GraphQL field will be non-nullable.

Allowed libraries

Specify which icon libraries to enable in the dashboard picker (Heroicons, Radix Icons, Lucide, VS Code Icons, Feather, Phosphor).

## Common Use Cases

### Navigation Icons

Perfect for menu items, sidebar navigation, and toolbar buttons:

```
import { Icon } from 'basehub/react-icon'

export const Navigation = ({ menuItems }) => {
  return (
    <nav>
      {menuItems.map((item) => (
        <a key={item._id} href={item.href} className="nav-link">
          <Icon
            content={item.icon}
            components={{
              svg: (props) => (
                <svg
                  {...props}
                  className="w-5 h-5 mr-2 text-gray-600 hover:text-blue-600"
                />
              ),
            }}
          />
          {item.label}
        </a>
      ))}
    </nav>
  )
}
```

### Social Media Links

Ideal for footer social links, contact sections, and profile pages:

```

import { Icon } from 'basehub/react-icon'

export const SocialFooter = ({ socialLinks }) => {
  return (
    <div className="flex space-x-4">
      {socialLinks.map((link) => (
        <a
          key={link._id}
          href={link.href}
          className="social-link"
          target="_blank"
          rel="noopener noreferrer"
          aria-label={link.label}
        >
          <Icon
            content={link.icon}
            components={{
              svg: (props) => (
                <svg
                  {...props}
                  className="w-6 h-6 text-gray-400 hover:text-white transition-colors"
                />
              ),
            }}
          />
        </a>
      ))}
    </div>
  )
}
```

### Feature Cards

Great for showcasing features, services, or benefits with visual indicators:

```

import { Icon } from 'basehub/react-icon'

export const FeatureGrid = ({ features }) => {
  return (
    <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
      {features.map((feature) => (
        <div key={feature._id} className="feature-card">
          <div className="icon-container">
            <Icon
              content={feature.icon}
              components={{
                svg: (props) => (
                  <svg {...props} className="w-12 h-12 text-blue-600 mb-4" />
                ),
              }}
            />
          </div>
          <h3 className="text-xl font-semibold mb-2">{feature.title}</h3>{' '}
          <p className="text-gray-600">{feature.description}</p>{' '}
        </div>
      ))}
    </div>
  )
}
```

## Best Practices

*   **Use small CSS style tweaks in basehub** to keep code cleaner.
    
*   **Optimize SVG content** by replacing base64 encoded images to url’s. F.E: you can upload images to basehub and use the url as the source of image tags in your' svg’s.
    
*   **Use** `currentColor` for fills and strokes to inherit text color from parent elements