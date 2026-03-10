# Source: https://seed-design.io/breeze/llms-full.txt

file: components/animate-number.mdx

# Animate Number

숫자를 부드럽게 애니메이션하는 유틸리티 컴포넌트

## Preview

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

Installation \[#installation]

Dependency:

- npm: npm install motion
- pnpm: pnpm add motion
- yarn: yarn add motion
- bun: bun add motion

Snippet:

- npm: npx @seed-design/cli@latest add breeze:animate-number
- pnpm: pnpm dlx @seed-design/cli@latest add breeze:animate-number
- yarn: yarn dlx @seed-design/cli@latest add breeze:animate-number
- bun: bun x @seed-design/cli@latest add breeze:animate-number

<BreezeManualInstallation name="animate-number" />

Configuration \[#configuration]

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

Props \[#props]

- `value`
  - type: `number`
  - default: `undefined`
  - required: `true`
  - description: 표시할 숫자 값
- `fontSize`
  - type: `string | number | undefined`
  - default: `48`
  - required: `false`
  - description: 폰트 크기
- `fontWeight`
  - type: `Property.FontWeight | undefined`
  - default: `"bold"`
  - required: `false`
  - description: 폰트 굵기
- `color`
  - type: `string | undefined`
  - default: `"currentColor"`
  - required: `false`
  - description: 텍스트 색상
- `showComma`
  - type: `boolean | undefined`
  - default: `false`
  - required: `false`
  - description: 천 단위 구분 쉼표 표시
- `showGradient`
  - type: `boolean | undefined`
  - default: `false`
  - required: `false`
  - description: 위아래 그라디언트 마스크 표시
- `gradientHeight`
  - type: `number | undefined`
  - default: `20`
  - required: `false`
  - description: 그라디언트 마스크 높이 (px)
- `containerStyle`
  - type: `React.CSSProperties | undefined`
  - default: `undefined`
  - required: `false`
  - description: 컨테이너 스타일
- `className`
  - type: `string | undefined`
  - default: `undefined`
  - required: `false`
  - description: 추가 클래스명

Examples \[#examples]

Comma \[#comma]

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

Gradient \[#gradient]

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

Custom Style \[#custom-style]

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