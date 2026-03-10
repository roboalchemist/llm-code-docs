# <Toolbar />

> The official BaseHub toolbar to manage draft mode and switch branches in your site previews.

```
import { Toolbar } from 'basehub/next-toolbar'
```

The Toolbar takes care of setting and managing the draftMode key without any other configuration or manual fetch to the BaseHub API.

![](https://assets.basehub.com/7b31fb4b/Fd2hLFehKGMaIrJnwsjH5/screenshot-2024-06-11-at-18.56.51.png?width=3840&quality=90&format=auto)

Toolbar - Draft Mode Enabled

![](https://assets.basehub.com/7b31fb4b/KfTDhoUO7Bm2KxDEdB3gY/screenshot-2024-06-11-at-18.57.01.png?width=3840&quality=90&format=auto)

Toolbar - Draft Mode disabled

## Props

\[data-radix-scroll-area-viewport\]{scrollbar-width:none;-ms-overflow-style:none;-webkit-overflow-scrolling:touch;}\[data-radix-scroll-area-viewport\]::-webkit-scrollbar{display:none}

Key

Type

Description

`forceDraft`

`boolean`

Will force the draft mode for the entire site when present.

## Example

```
import { Toolbar } from 'basehub/next-toolbar'

export default async function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode
}>) {
  return (
    <html lang="en">
      <Toolbar />
      <body>
        <ThemeProvider>
          <Header />
          {children}
          <Footer />
        </ThemeProvider>
      </body>
    </html>
  )
}
```