# Source: https://redocly.com/learn/arazzo/testing-arazzo-workflows.md

# Testing API Workflows with Respect

You've documented your Warp API workflow to nab Tesla's blueprint from 1889ânow it's time to test it.
Redocly's new tool, **Respect**, launched in 2025, runs Arazzo files with a command like `npx @redocly/cli@latest respect warp.arazzo.yaml --input token=your-warp-token`.
It executes your time-travel mission against the Warp API, showing you if every anchor, jump, and return works as planned. Let's dive into how Respect tests your Warp workflow, run our Tesla mission, and unpack the output to ensure we don't get stuck in the past.

## Why test with Respect?

Arazzo workflows are actionable scripts, not just docs.

Respect takes your Warp API stepsâsetting anchors, creating timelines, traveling through timeâand runs them live (or against mocks), giving you real results.

Testing with Respect:

- **Confirms execution**: Checks if the sequence (anchor â timeline â travel) flows smoothly.
- **Spots failures**: Catches issues like bad tokens or paradox-inducing jumps early.
- **Delivers output**: Shows step-by-step success or failureâdid Tesla's blueprint make it back?


Unlike `npx @redocly/cli@latest lint` (syntax checking), Respect *executes* the workflow, hitting Warp's endpoints with your inputs.
It's like a time machine simulatorâpress go and see where you land.

## Setting up Respect

You'll need:

- **Redocly CLI**: We'll use `npx` to get the latest version of the CLI.
- **Arazzo file**: We'll use `warp.arazzo.yaml` and `warp.openapi.yaml` from the [documentation article](/learn/arazzo/arazzo-walkthrough) - click the download button at the top-right of the file list.
- **Warp token**: A bearer token for Warp's `bearerAuth` security (you can make up any token such as `abc123`).


## Testing the Tesla blueprint workflow

Execute it:


```bash
npx @redocly/cli@latest respect warp.arazzo.yaml --input token=abc123
```

The `--input token=abc123` passes the Warp token to the workflow, mapping to its security needs.

## Decoding the output

Respect runs each step, sending requests to Warp's API and logging the results. Here's a possible output (hypothetical, based on Respect's purpose):


```bash
Running workflow warp.arazzo.yaml / missionLostInvention

  â POST /anchors - step setAnchorToCurrentTime
Â Â Â Â â status code check (Response code 201 matches one of description codes: [201, 409])
Â Â Â Â â content-type check
Â Â Â Â â schema check

  â POST /timelines - step createTimelineTo1889
Â Â Â Â â status code check (Response code 201 matches one of description codes: [201])
Â Â Â Â â content-type check
Â Â Â Â â schema check

  â POST /travels - step travelTo1889
Â Â Â Â â status code check (Response code 200 matches one of description codes: [200, 400])
Â Â Â Â â content-type check
Â Â Â Â â schema check

  â POST /items - step findAndRegisterBlueprint
Â Â Â Â â status code check (Response code 200 matches one of description codes: [200, 409])
Â Â Â Â â content-type check
Â Â Â Â â schema check

  â POST /paradox-checks - step avoidParadox
Â Â Â Â â success criteria check
Â Â Â Â â success criteria check
Â Â Â Â â status code check (Response code 200 matches one of description codes: [200, 400])
Â Â Â Â â content-type check
Â Â Â Â â schema check

  â POST /travels - step returnToPresent
Â Â Â Â â status code check (Response code 200 matches one of description codes: [200, 400])
Â Â Â Â â content-type check
Â Â Â Â â schema check


Â Â Summary for warp.arazzo.yaml
Â Â 
Â Â Workflows: 1 passed, 1 total
Â Â Steps: 6 passed, 6 total
Â Â Checks: 20 passed, 20 total
Â Â Time: 996ms


âââââââââââââââââââââââââââââââââââââââââââââââââââââââ¬âââââââââââââ¬ââââââââââ¬ââââââââââ¬âââââââââââ¬ââââââââââ
â Filename                                            â Workflows  â Passed  â Failed  â Warnings â Skipped â
âââââââââââââââââââââââââââââââââââââââââââââââââââââââ¼âââââââââââââ¼ââââââââââ¼ââââââââââ¼âââââââââââ¼ââââââââââ¤
â â warp.arazzo.yaml                                  â 1          â 1       â -       â -        â -       â
âââââââââââââââââââââââââââââââââââââââââââââââââââââââ´âââââââââââââ´ââââââââââ´ââââââââââ´âââââââââââ´ââââââââââ
```

Respect checks the status code, content-type, and schema of each step automatically.
In addition, it checks the success criteria of each step, if defined.

## Enhancing with Respect options

The Respect docs offer handy flags:

Verbose Mode: Add `--verbose` for detailed logs (truncated to the first step in the example below because it is verbose):


```bash
npx @redocly/cli@latest respect warp.arazzo.yaml --input token=abc123 --verbose

Running workflow warp.arazzo.yaml / missionLostInvention

  â POST /anchors - step setAnchorToCurrentTime

Â Â Â Â Request URL: https://warp-multi-sidebars.redocly.app/_mock/apis/anchors
Â Â Â Â Request Headers:
Â Â Â Â Â Â content-type: application/json
Â Â Â Â Â Â accept: application/json
Â Â Â Â Â Â authorization: ********
Â Â Â Â Request Body:
Â Â Â Â Â Â {
Â Â Â Â Â Â   "timestamp": "2024-09-16T05:04:00Z",
Â Â Â Â Â Â   "description": "Home Base - Start of Tesla Mission"
Â Â Â Â Â Â }


Â Â Â Â Response status code: 201
Â Â Â Â Response time: 214 ms
Â Â Â Â Response Body:
Â Â Â Â Â Â {
Â Â Â Â Â Â   "id": "anc_mel2c9ba",
Â Â Â Â Â Â   "timestamp": "2024-09-16T05:04:00Z",
Â Â Â Â Â Â   "description": "Home Base - Start of Tesla Mission"
Â Â Â Â Â Â }

Â Â Â Â â status code check (Response code 201 matches one of description codes: [201, 409])
Â Â Â Â â content-type check
Â Â Â Â â schema check
```

## Why it matters

Respect turns your Warp Arazzo file into a live test, proving the Tesla blueprint mission worksâor doesn't.
It's not just theory; it's execution, catching bugs before they strand you in 1889.
For Warp's team, it's a QA step that ensures reliable time travel, and the output can plug into CI/CD for automated checks.