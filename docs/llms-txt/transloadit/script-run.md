# Source: https://transloadit.com/docs/robots/script-run.md

This Robot allows you to run arbitrary `JavaScript` as part of the Assemblyexecution process. The Robot is invoked automatically when there are Assembly Instructions containing `${...}`:

![](/_next/static/media/copy.8f7d2926.svg?dpl=dpl_GAEaNRfbaNgVy6q3c3ke5o1s9Xtk)

```json
{
  "robot": "/image/resize",
  "width": "${Math.max(file.meta.width, file.meta.height)}"
}

```

You can also invoke this Robot directly, leaving out the `${...}`:

![](/_next/static/media/copy.8f7d2926.svg?dpl=dpl_GAEaNRfbaNgVy6q3c3ke5o1s9Xtk)

```json
{
  "robot": "/script/run",
  "script": "Math.max(file.meta.width, file.meta.height)"
}

```

When accessing arrays, the syntax is the same as in any JavaScript program:

![](/_next/static/media/copy.8f7d2926.svg?dpl=dpl_GAEaNRfbaNgVy6q3c3ke5o1s9Xtk)

```json
{
  "robot": "/image/resize",
  "width": "${file.meta.faces[0].width * 2}"
}

```

Compared to only accessing an Assembly Variable:

![](/_next/static/media/copy.8f7d2926.svg?dpl=dpl_GAEaNRfbaNgVy6q3c3ke5o1s9Xtk)

```json
{
  "robot": "/image/resize",
  "width": "${file.meta.faces[0].width}"
}

```

For more information, see [Dynamic Evaluation](/docs/topics/dynamic-evaluation.md).
