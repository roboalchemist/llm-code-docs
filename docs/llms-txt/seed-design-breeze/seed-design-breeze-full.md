# Seed Design Breeze Documentation

Source: https://seed-design.io/breeze/llms-full.txt

---

file: components/animate-number.mdx

# Animate Number

숫자를 부드럽게 애니메이션하는 유틸리티 컴포넌트



<ComponentExample name="breeze/animate-number/preview">
  ```tsx
  import AnimateNumber from "seed-design/breeze/animate-number/animate-number";
  import { ActionButton } from "seed-design/ui/action-button";
  import { HStack } from "@seed-design/react";
  import { useState } from "react";

  export default function AnimateNumberPreview() {
    const [value, setValue] = useState(1);

    return (
      <div className="flex flex-col items-center gap-8">
        <AnimateNumber
          value={value}
          fontSize="6rem"
          fontWeight="bold"
          color="#333"
          showComma
          showGradient
          gradientHeight={10}
        />
        <HStack gap="10px">
          <ActionButton size="small" variant="neutralSolid" onClick={() => setValue(value - 1)}>
            -1
          </ActionButton>
          <ActionButton size="small" variant="neutralSolid" onClick={() => setValue(value + 1)}>
            +1
          </ActionButton>
        </HStack>
      </div>
    );
  }
  ```
</ComponentExample>

## Installation

Dependency:

<CodeBlockTabs defaultValue="npm" groupId="package-manager" persist>
  <CodeBlockTabsList>
    <CodeBlockTabsTrigger value="npm">
      npm
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="pnpm">
      pnpm
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="yarn">
      yarn
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="bun">
      bun
    </CodeBlockTabsTrigger>
  </CodeBlockTabsList>

  <CodeBlockTab value="npm">
    ```bash
    npm install motion
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm add motion
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn add motion
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bun add motion
    ```
  </CodeBlockTab>
</CodeBlockTabs>

Snippet:

<CodeBlockTabs defaultValue="npm" groupId="package-manager" persist>
  <CodeBlockTabsList>
    <CodeBlockTabsTrigger value="npm">
      npm
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="pnpm">
      pnpm
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="yarn">
      yarn
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="bun">
      bun
    </CodeBlockTabsTrigger>
  </CodeBlockTabsList>

  <CodeBlockTab value="npm">
    ```bash
    npx @seed-design/cli@latest add breeze:animate-number
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm dlx @seed-design/cli@latest add breeze:animate-number
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn dlx @seed-design/cli@latest add breeze:animate-number
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bun x @seed-design/cli@latest add breeze:animate-number
    ```
  </CodeBlockTab>
</CodeBlockTabs>

<BreezeManualInstallation name="animate-number" />

## Configuration

animate-number 컴포넌트는 motion의 `m.` 컴포넌트를 사용합니다. lazy loading을 위해 프로젝트에 MotionProvider를 설정해야 합니다.

자세한 내용은 [Motion Lazy Motion 문서](https://motion.dev/docs/react-lazy-motion)를 참고하세요.

```tsx title="MotionProvider.tsx"
"use client";

import { LazyMotion } from "motion/react";
import type { ReactNode } from "react";

const loadFeatures = () => import("motion/react").then((res) => res.domAnimation);

export function MotionProvider({ children }: { children: ReactNode }) {
  return <LazyMotion features={loadFeatures}>{children}</LazyMotion>;
}
```

```tsx title="index.tsx"
import { createRoot } from 'react-dom/client'
import App from './App.tsx'
import { MotionProvider } from './MotionProvider.tsx'

createRoot(document.getElementById('root')!).render(
  <MotionProvider>
    <App />
  </MotionProvider>
)
```

## Props

<TypeTable
  type={{
    value: {
        "type": "number",
        "default": undefined,
        "required": true,
        description: <><p>{"표시할 숫자 값"}</p></>
    },

    fontSize: {
        "type": "string | number | undefined",
        "default": "48",
        "required": false,
        description: <><p>{"폰트 크기"}</p></>
    },

    fontWeight: {
        "type": "Property.FontWeight | undefined",
        "default": "\"bold\"",
        "required": false,
        description: <><p>{"폰트 굵기"}</p></>
    },

    color: {
        "type": "string | undefined",
        "default": "\"currentColor\"",
        "required": false,
        description: <><p>{"텍스트 색상"}</p></>
    },

    showComma: {
        "type": "boolean | undefined",
        "default": "false",
        "required": false,
        description: <><p>{"천 단위 구분 쉼표 표시"}</p></>
    },

    showGradient: {
        "type": "boolean | undefined",
        "default": "false",
        "required": false,
        description: <><p>{"위아래 그라디언트 마스크 표시"}</p></>
    },

    gradientHeight: {
        "type": "number | undefined",
        "default": "20",
        "required": false,
        description: <><p>{"그라디언트 마스크 높이 (px)"}</p></>
    },

    containerStyle: {
        "type": "React.CSSProperties | undefined",
        "default": undefined,
        "required": false,
        description: <><p>{"컨테이너 스타일"}</p></>
    },

    className: {
        "type": "string | undefined",
        "default": undefined,
        "required": false,
        description: <><p>{"추가 클래스명"}</p></>
    }
}}
/>

## Examples

### Comma

<ComponentExample name="breeze/animate-number/comma">
  ```tsx
  import AnimateNumber from "seed-design/breeze/animate-number/animate-number";
  import { ActionButton } from "seed-design/ui/action-button";
  import { useState } from "react";

  export default function AnimateNumberComma() {
    const [value, setValue] = useState(1234);

    return (
      <div className="flex flex-col items-center gap-6">
        <AnimateNumber value={value} fontSize="3rem" showComma />

        <ActionButton
          size="small"
          variant="neutralSolid"
          onClick={() => setValue(Math.floor(Math.random() * 99999) + 1)}
        >
          랜덤 숫자 (1-99999)
        </ActionButton>
      </div>
    );
  }
  ```
</ComponentExample>

### Gradient

<ComponentExample name="breeze/animate-number/gradient">
  ```tsx
  import AnimateNumber from "seed-design/breeze/animate-number/animate-number";
  import { ActionButton } from "seed-design/ui/action-button";
  import { useState } from "react";

  export default function AnimateNumberGradient() {
    const [value, setValue] = useState(999);

    return (
      <div className="flex flex-col items-center gap-6">
        <AnimateNumber value={value} fontSize="4rem" showGradient gradientHeight={20} />

        <ActionButton
          size="small"
          variant="neutralSolid"
          onClick={() => setValue(Math.floor(Math.random() * 99999) + 1)}
        >
          랜덤 숫자 (1-99999)
        </ActionButton>
      </div>
    );
  }
  ```
</ComponentExample>

### Custom Style

<ComponentExample name="breeze/animate-number/custom-style">
  ```tsx
  import AnimateNumber from "seed-design/breeze/animate-number/animate-number";
  import { ActionButton } from "seed-design/ui/action-button";
  import { HStack } from "@seed-design/react";
  import { useState } from "react";

  export default function AnimateNumberCustomStyle() {
    const [value, setValue] = useState(42);

    return (
      <div className="flex flex-col items-center gap-6">
        <AnimateNumber
          value={value}
          fontSize="2.5rem"
          fontWeight="600"
          color="#FF6B00"
          containerStyle={{ padding: "1rem" }}
        />

        <HStack gap="10px">
          <ActionButton
            size="small"
            variant="neutralSolid"
            onClick={() => setValue(Math.floor(Math.random() * 99999) + 1)}
          >
            랜덤 숫자
          </ActionButton>
        </HStack>
      </div>
    );
  }
  ```
</ComponentExample>
