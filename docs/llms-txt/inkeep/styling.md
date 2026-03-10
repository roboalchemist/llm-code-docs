# Source: https://docs.inkeep.com/talk-to-your-agents/customization/styling

# Style Components (/talk-to-your-agents/customization/styling)

Customize the appearance of Inkeep's components.



The style configuration provides comprehensive settings for customizing the appearance of Inkeep widgets. This includes theming, typography, spacing, and component-specific styles.

## Theme Configuration

The theme configuration is defined through the `UserTheme` interface which extends `Partial<IkpTheme>`. This allows for deep customization of the widget's appearance.

```typescript
import { type InkeepBaseSettings } from "@inkeep/cxkit-types";

const baseSettings: InkeepBaseSettings = {
  theme: {
    // Basic color customization
    primaryColors: {
      primary: "#26D6FF",
      secondary: "#6366F1",
    },

    // Syntax highlighter themes
    syntaxHighlighter: {
      lightTheme: themes.github,
      darkTheme: themes.dracula,
    },

    // Custom styles injection
    styles: [
      {
        key: "google-fonts",
        type: "link",
        value:
          "https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap",
      },
      {
        key: "custom-theme",
        type: "style",
        value: `
          .ikp-ai-chat-message {
            border-radius: 8px;
            padding: 12px;
          }
          [data-theme='dark'] .ikp-ai-chat-message {
            background: #2D3748;
          }
        `,
      },
    ],

    // CSS variables container class name
    varsClassName: "ikp-variables",

    // Disable loading the default font for the widgets
    disableLoadingDefaultFont: true,
  },
};
```

### Theme Properties

#### Primary Colors

The `primaryColors` property allows you to define the color variations used throughout the widget. It accepts the following color options:

```typescript
primaryColors: {
  textBold?: string         // Bold text color
  textSubtle?: string       // Subtle text color
  lighter?: string          // Lightest shade
  light?: string           // Light shade
  lightSubtle?: string     // Subtle light shade
  medium?: string          // Medium shade
  mediumSubtle?: string    // Subtle medium shade
  strong?: string          // Strong shade
  stronger?: string        // Stronger shade
  textColorOnPrimary?: string     // Text color on primary background
}
```

All colors should be provided as valid CSS color values (hex, rgb, hsl, etc). Each property is optional, allowing you to customize only the specific color variations you need.

#### Syntax Highlighter Theme

The `syntaxHighlighter` property lets you configure different themes for code blocks in light and dark modes.

By default, the Prism syntax highlighting theme we use is [oneLight](https://github.com/FormidableLabs/prism-react-renderer/blob/master/packages/prism-react-renderer/src/themes/oneLight.ts) in light mode and [vsDark](https://github.com/FormidableLabs/prism-react-renderer/blob/master/packages/prism-react-renderer/src/themes/vsDark.ts) in dark mode. To use a different theme, you can provide it in the theme.syntaxHighlighter prop.

```typescript
syntaxHighlighter: {
  lightTheme: themes.github,  // Theme for light mode
  darkTheme: themes.dracula   // Theme for dark mode
}
```

You can use published Prism themes or [create your own](https://github.com/PrismJS/prism-themes).

#### Custom Styles

The `styles` property allows injection of custom styles through two methods:

1. External Resources (type: 'link'):

```typescript
{
  key: 'google-fonts',
  type: 'link',
  value: 'https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap'
}
```

2. Inline CSS (type: 'style'):

```typescript
{
  key: 'custom-theme',
  type: 'style',
  value: `
    .ikp-ai-chat-message {
      border-radius: 8px;
      padding: 12px;
    }
  `
}
```

Each style entry requires:

* `key`: A unique identifier to prevent duplicates and enable updates
* `type`: Either 'link' for external resources or 'style' for inline CSS
* `value`: The style content (URL for links or CSS code for styles)

#### Variables Class Name

The `varsClassName` property specifies the class name for the container that holds CSS variables:

```typescript
varsClassName: "ikp-variables"; // Default value
```

This class is added to a wrapper div that provides theming context.

## Color Mode Configuration

The color mode configuration allows you to control how the widget handles light and dark modes. This is configured through the `colorMode` property in the base settings:

```typescript
const baseSettings: InkeepBaseSettings = {
  colorMode: {
    // Force a specific color mode
    forcedColorMode?: string,

    // Enable system color mode detection
    enableSystem?: boolean,

    // Sync with external element
    sync?: {
      // Element to watch for color mode changes
      target: HTMLElement | string,

      // Attributes to monitor
      attributes: string[],

      // Function to determine dark mode
      isDarkMode: (attributes: Record<string, string | null>) => boolean,

      // Optional callback for color mode changes
      onChange?: (colorMode: string) => void
    }
  }
}
```

### Color Mode Properties

#### Forced Color Mode

Use `forcedColorMode` to explicitly set the color mode for the current page:

```typescript
colorMode: {
  forcedColorMode: "dark"; // Forces dark mode
}
```

#### System Color Mode

Enable `enableSystem` to automatically switch between dark and light modes based on the user's system preferences:

```typescript
colorMode: {
  enableSystem: true; // Follows system preference
}
```

#### Color Mode Sync

The `sync` property allows you to synchronize the widget's color mode with your application's theme:

```typescript
colorMode: {
  sync: {
    // Watch the document root for theme changes
    target: document.documentElement,

    // Monitor the data-theme attribute
    attributes: ['data-theme'],

    // Determine dark mode based on attribute value
    isDarkMode: (attrs) => attrs['data-theme'] === 'dark',

    // Optional: Handle color mode changes
    onChange: (mode) => console.log(`Color mode changed to: ${mode}`)
  }
}
```

Common sync configurations:

1. **Data Attribute Sync**:

```typescript
{
  target: document.documentElement,
  attributes: ['data-theme'],
  isDarkMode: (attrs) => attrs['data-theme'] === 'dark'
}
```

2. **Class-based Sync**:

```typescript
{
  target: document.documentElement,
  attributes: ['class'],
  isDarkMode: (attrs) => attrs['class']?.includes('dark-mode')
}
```

## Using CSS Variables

Inkeep provides a set of CSS variables that you can use to customize the widget's appearance. These variables are prefixed with `--ikp-` and are available within the scope of the widget.

### Basic Usage

You can use Inkeep CSS variables within your stylesheets to customize elements. For example:

```css
.ikp-chat-button__button {
  background: var(--ikp-colors-inkeep-primary-medium);
}
```

### Dark Mode Styling

To apply specific styles for dark mode, use the `[data-theme='dark']` attribute selector:

```css
[data-theme="dark"] .ikp-chat-button__button {
  background: #353e52;
}
```

## Customizing Icons

### AI Assistant Avatar

The AI assistant avatar can be customized through the `aiChatSettings` using the `aiAssistantAvatar` property:

it's either a string URL or an object to specify light and dark mode avatars:

```typescript
aiAssistantAvatar: {
  light: string;
  dark?: string;
}
```

### User Avatar

The user avatar can be customized using the `userAvatar` property in the `aiChatSettings`.

```typescript
import { type InkeepAIChatSettings } from "@inkeep/cxkit-react";

export const aiChatSettings: InkeepAIChatSettings = {
  aiAssistantAvatar: "http://example.com/assistant-avatar.png",
  userAvatar: "http://example.com/user-avatar.png",
  // ...rest of aiChatSettings
};
```

### Custom Icons

You can customize various icons throughout the widget by providing a `customIcons` dictionary in the `baseSettings`. Each icon can be either a built-in icon or a custom SVG/image.

#### Available Icons

| Icon Name           | Description                                                                                  |
| ------------------- | -------------------------------------------------------------------------------------------- |
| search              | Search icon in search bar                                                                    |
| thumbsUp            | Thumbs up icon                                                                               |
| thumbsDown          | Thumbs down icon                                                                             |
| messageCopy         | Copy message icon                                                                            |
| codeCopy            | Copy code icon in code header                                                                |
| openLinkInNewTab    | Used on hover in chat citations and search results (when `shouldOpenLinksInNewTab` is true)  |
| openLinkInSameTab   | Used on hover in chat citations and search results (when `shouldOpenLinksInNewTab` is false) |
| breadcrumbSeparator | Breadcrumb separator icon                                                                    |
| switchToSearch      | Switch to search icon                                                                        |
| switchToChat        | Switch to chat icon                                                                          |
| chatSubmit          | Chat submit icon                                                                             |
| close               | Close icon                                                                                   |
| info                | Info icon next to the disclaimer and chat mode toggle                                        |
| command             | Command icon in search bar                                                                   |

#### Example Configuration

```typescript
import { type InkeepBaseSettings } from "@inkeep/cxkit-react";

export const baseSettings: InkeepBaseSettings = {
  customIcons: {
    // Using a built-in icon
    search: {
      builtIn: "IoSearch",
    },

    // Using custom SVG/image URLs
    thumbsUp: {
      custom: "/path/to/thumbs-up.svg",
    },
    thumbsDown: {
      custom: "/path/to/thumbs-down.svg",
    },
    messageCopy: {
      custom: "/path/to/message-copy.svg",
    },
    codeCopy: {
      custom: "/path/to/code-copy.svg",
    },
    openLinkInNewTab: {
      custom: "path/to/open-link-in-new-tab.svg",
    },
    openLinkInSameTab: {
      custom: "path/to/open-link-in-same-tab.svg",
    },
    breadcrumbSeparator: {
      custom: "path/to/breadcrumb-separator.svg",
    },
    switchToSearch: {
      custom: "/path/to/switch-to-search.svg",
    },
    switchToChat: {
      custom: "/path/to/switch-to-chat.svg",
    },
    chatSubmit: {
      custom: "/path/to/chat-submit.svg",
    },
    close: {
      custom: "/path/to/close.svg",
    },
    info: {
      custom: "/path/to/info.svg",
    },
    command: {
      custom: "/path/to/command.svg",
    },
  },
  // ...rest of baseSettings
};
```

> If the url for a `custom` icon is a `.svg` file it will be rendered as an `<svg>`, all other file types will be rendered using an `<Image>` tag.

## Default Theme

The default theme includes these core settings:

### Typography

```typescript
fontFamily: {
  heading: "'Space Grotesk', system-ui, sans-serif",
  body: "'Inter', system-ui, sans-serif",
  mono: "'Fira Code', monospace",
},
fontSize: {
  '3xs': '0.45rem',
  '2xs': '0.625rem',
  xs: '0.75rem',
  sm: '0.875rem',
  md: '1rem',
  lg: '1.125rem',
  xl: '1.25rem',
  '2xl': '1.5rem',
  '3xl': '1.875rem',
  '4xl': '2.25rem',
  '5xl': '3rem',
  '6xl': '3.75rem',
  '7xl': '4.5rem',
  '8xl': '6rem',
  '9xl': '8rem',
}
```

### Z-Index

```typescript
zIndex: {
  hide: -1,
  auto: 'auto',
  base: 0,
  docked: 10,
  dropdown: 1000,
  sticky: 1100,
  banner: 1200,
  overlay: 1300,
  modal: 1400,
  popover: 1500,
  skipLink: 1600,
  toast: 1700,
  tooltip: 1800,
}
```

## Component Class Names

All component class names are prefixed with `ikp-`. Here's the complete list of available class names:

<>
  ### Chat Components

  ```css
  ikp-ai-chat-wrapper
  ikp-ai-chat-root
  ikp-ai-chat-header
  ikp-ai-chat-header__toolbar
  ikp-ai-chat-header__toolbar-header
  ikp-ai-chat-header__toolbar-header-wrapper
  ikp-ai-chat-content
  ikp-ai-chat-content-scroll-area
  ikp-ai-chat-content-scroll-area__viewport
  ikp-ai-chat-content-scroll-area__scrollbar
  ikp-ai-chat-content-scroll-area__thumb
  ikp-ai-chat-content-scroll-area__corner
  ikp-ai-chat-disclaimer
  ikp-ai-chat-disclaimer-label
  ikp-ai-chat-disclaimer-trigger
  ikp-ai-chat-disclaimer-content
  ikp-ai-chat-disclaimer-text
  ikp-ai-chat-disclaimer-arrow
  ikp-ai-chat-example-questions
  ikp-ai-chat-example-questions-label
  ikp-ai-chat-example-questions-list
  ikp-ai-chat-example-question
  ikp-ai-chat-example-question-button
  ikp-ai-chat-workflows
  ikp-ai-chat-workflows-label
  ikp-ai-chat-workflows-list
  ikp-ai-chat-workflow
  ikp-ai-chat-workflow__icon
  ikp-ai-chat-messages
  ikp-ai-chat-message-wrapper
  ikp-ai-chat-message-header
  ikp-ai-chat-message-loading
  ikp-ai-chat-message-avatar
  ikp-ai-chat-message-avatar-fallback
  ikp-ai-chat-message-avatar-image
  ikp-ai-chat-message-avatar-content
  ikp-ai-chat-message-name
  ikp-ai-chat-message-content-wrapper
  ikp-ai-chat-message-content
  ikp-ai-chat-message-attachments
  ikp-ai-chat-message-attachments__list
  ikp-ai-chat-message-attachments__item
  ikp-ai-chat-message-attachments__item-icon
  ikp-ai-chat-message-attachments__item-title
  ikp-ai-chat-message-attachments-preview
  ikp-ai-chat-message-attachments-preview__overlay
  ikp-ai-chat-message-attachments-preview__content
  ikp-ai-chat-message-attachments-preview__header
  ikp-ai-chat-message-attachments-preview__close
  ikp-ai-chat-message-attachments-preview__body
  ikp-ai-chat-message-part
  ikp-ai-chat-message-toolbar
  ikp-ai-chat-message-custom-actions
  ikp-ai-chat-message-custom-action
  ikp-ai-chat-message-action
  ikp-ai-chat-message-sources
  ikp-ai-chat-message-sources__header
  ikp-ai-chat-message-sources__list
  ikp-ai-chat-message-source-item
  ikp-ai-chat-message-source-item__icon
  ikp-ai-chat-message-source-item__breadcrumbs
  ikp-ai-chat-message-source-item__breadcrumb
  ikp-ai-chat-message-source-item__breadcrumb-icon
  ikp-ai-chat-message-source-item__title
  ikp-ai-chat-message-source-item__tag
  ikp-ai-chat-message-source-item__description
  ikp-ai-chat-message-source-item__description-part
  ikp-ai-chat-message-source-item__indicator
  ikp-ai-chat-footer
  ikp-ai-chat-input__fieldset
  ikp-ai-chat-input__group
  ikp-ai-chat-input
  ikp-ai-chat-input__send-button
  ikp-ai-chat-input__send-button-icon
  ikp-ai-chat-attachments-bar
  ikp-ai-chat-attachments-bar__list
  ikp-ai-chat-attachments-bar__attachment
  ikp-ai-chat-attachments-bar__attachment-icon
  ikp-ai-chat-attachments-bar__attachment-title
  ikp-ai-chat-attachments-bar__attachment-delete
  ikp-ai-chat-attachments-bar__actions
  ikp-ai-chat-attachments-bar__info-tip
  ikp-ai-chat-attachments-bar__info-tip-icon
  ikp-ai-chat-attachments-bar__info-tip-arrow
  ikp-ai-chat-attachments-bar__info-tip-text
  ikp-ai-chat-attachments-bar__inputs
  ikp-ai-chat-attachments-bar__input
  ikp-ai-chat-attachments-bar__input-icon
  ikp-ai-chat-attachments-bar__modal
  ikp-ai-chat-attachments-bar__modal-overlay
  ikp-ai-chat-attachments-bar__modal-content
  ikp-ai-chat-attachments-bar__modal-header
  ikp-ai-chat-attachments-bar__modal-close
  ikp-ai-chat-attachments-bar__modal-body
  ikp-ai-chat-attachments-bar__modal-heading
  ikp-ai-chat-attachments-bar__modal-description
  ikp-ai-chat-attachments-bar__modal-help
  ikp-ai-chat-attachments-bar__form
  ikp-ai-chat-attachments-bar__form-title
  ikp-ai-chat-attachments-bar__form-title-label
  ikp-ai-chat-attachments-bar__form-title-input
  ikp-ai-chat-attachments-bar__form-title-error
  ikp-ai-chat-attachments-bar__form-content
  ikp-ai-chat-attachments-bar__form-content-label
  ikp-ai-chat-attachments-bar__form-content-input
  ikp-ai-chat-attachments-bar__form-content-error
  ikp-ai-chat-attachments-bar__form-submit-button
  ikp-ai-chat-action-bar
  ikp-ai-chat__chat-actions
  ikp-ai-chat__chat-action
  ikp-ai-chat__chat-action-label
  ikp-ai-chat__chat-action-feeback
  ikp-ai-chat-help-actions
  ikp-ai-chat-help-action
  ikp-ai-chat-help-actions__trigger
  ikp-ai-chat-help-actions__menu
  ikp-ai-chat-help-actions__menu-arrow
  ikp-ai-chat-help-actions__menu-item
  ikp-ai-chat-help-actions_menu-item-icon
  ikp-ai-chat-tagline__container
  ikp-ai-chat-tagline__text
  ikp-ai-chat-tagline__logo
  ikp-ai-chat-tagline__brand-name
  ikp-ai-chat-feedback-modal
  ikp-ai-chat-feedback-modal__overlay
  ikp-ai-chat-feedback-modal__content
  ikp-ai-chat-feedback-modal__header
  ikp-ai-chat-feedback-modal__close
  ikp-ai-chat-feedback-modal__body
  ikp-ai-chat-feedback-form
  ikp-ai-chat-feedback-item
  ikp-ai-chat-feedback-item__checkbox
  ikp-ai-chat-feedback-item__checkbox-indicator
  ikp-ai-chat-feedback-item__label
  ikp-ai-chat-feedback-item__description
  ikp-ai-chat-feedback-form__submit-button
  ikp-ai-chat-form__wrapper
  ikp-ai-chat-form
  ikp-ai-chat-form__close
  ikp-ai-chat-form__header
  ikp-ai-chat-form__heading
  ikp-ai-chat-form__description
  ikp-ai-chat-form__content
  ikp-ai-chat-form__field
  ikp-ai-chat-form__field-label
  ikp-ai-chat-form__field-text
  ikp-ai-chat-form__field-email
  ikp-ai-chat-form__field-file
  ikp-ai-chat-form__field-text-area
  ikp-ai-chat-form__field-checkbox
  ikp-ai-chat-form__field-checkbox-indicator
  ikp-ai-chat-form__field-select
  ikp-ai-chat-form__field-select__trigger
  ikp-ai-chat-form__field-select__value
  ikp-ai-chat-form__field-select__icon
  ikp-ai-chat-form__field-select__content
  ikp-ai-chat-form__field-select__viewport
  ikp-ai-chat-form__field-select__item
  ikp-ai-chat-form__field-select__item-indicator
  ikp-ai-chat-form__field-select__item-text
  ikp-ai-chat-form__field-combobox__control
  ikp-ai-chat-form__field-combobox__positioner
  ikp-ai-chat-form__field-combobox__input
  ikp-ai-chat-form__field-combobox__trigger
  ikp-ai-chat-form__field-combobox__selected-tags
  ikp-ai-chat-form__field-combobox__content
  ikp-ai-chat-form__field-combobox__list
  ikp-ai-chat-form__field-combobox__list-empty
  ikp-ai-chat-form__field-combobox__item
  ikp-ai-chat-form__field-combobox__item-text
  ikp-ai-chat-form__field-combobox__item-indicator
  ikp-ai-chat-form__field-description
  ikp-ai-chat-form__field-error
  ikp-ai-chat-form__error
  ikp-ai-chat-form__footer
  ikp-ai-chat-form__cancel
  ikp-ai-chat-form__submit
  ikp-ai-chat-form__success
  ikp-ai-chat-form__success-heading
  ikp-ai-chat-form__success-message
  ikp-ai-chat-form__success-button
  ikp-ai-chat-link
  ```

  ### Markdown Components

  ```css
  ikp-codeblock-container
  ikp-codeblock-header
  ikp-codeblock-header-language
  ikp-codeblock-copy-button
  ikp-codeblock-highlighter-wrapper
  ikp-codeblock-highlighter
  ikp-codeblock-code
  ikp-markdown-h1
  ikp-markdown-h2
  ikp-markdown-p
  ikp-markdown-li
  ikp-markdown-ul
  ikp-markdown-ol
  ikp-markdown-link
  ikp-markdown-source-link
  ikp-markdown-table
  ikp-markdown-th
  ikp-markdown-td
  ikp-markdown-code
  ikp-markdown-input
  ikp-markdown-sup
  ikp-markdown-img
  ikp-markdown-hr
  ```

  ### Search Bar Components

  ```css
  ikp-search-bar__container
  ikp-search-bar__button
  ikp-search-bar__content-wrapper
  ikp-search-bar__text
  ikp-search-bar__icon
  ikp-search-bar__kbd-wrapper
  ikp-search-bar__cmd-icon
  ikp-search-bar__ctrl
  ikp-search-bar__kbd-shortcut-key
  ```

  ### Modal Components

  ```css
  ikp-modal
  ikp-modal__overlay
  ikp-modal__content
  ikp-modal__close
  ```

  ### Chat Button Components

  ```css
  ikp-chat-button__text
  ikp-chat-button__button
  ikp-chat-button__container
  ikp-chat-button__avatar-image
  ikp-chat-button__avatar-content
  ikp-chat-button__close-icon
  ```

  ### Miscellaneous Components

  ```css
  ikp-icon
  ikp-loading-indicator__text
  ikp-loading-indicator__dots
  ikp-loading-indicator__dot
  ikp-view_toggle
  ikp-view_toggle_button
  ikp-view_toggle_icon
  ```
</>
