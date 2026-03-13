# Source: https://docs.gitguardian.com/secrets-detection/secrets-detection-engine/validation.md

# Pre-Validators and Post-Validators

> Pre-validator and post-validator components of the detection engine that filter documents and validate matches to reduce false positives.

A `Detector` consists of three core components:

- **Pre-Validators**: These rules are applied before the detection process begins. They determine whether the detection should proceed.
- **Matchers**: Matchers are string extractors that identify and return matched strings, also known as "matches". Typically, matchers use regular expressions, but they can be more complex, such as detecting connection strings.
- **Post-Validators**: These rules are applied after the matchers. They validate the identified matches. Note that post-validators can be applied to a single match or to all matches found by the matcher.

## Pre-Validation

Pre-validators are an essential component of the secrets detection process. They serve as an initial filter, determining whether further analysis and detection should occur. Pre-validators apply specific rules and conditions before the actual detection process takes place. Their purpose is to ensure that documents meet certain criteria before scanning them. These criteria include checking for specific patterns in the content, filename, path or extensions, or banning minified JavaScript files. Pre-validators optimize the scanning process by focusing on relevant documents.

The following pre-validators are used by our secrets detection engine:

- `BanMinifiedPreValidator`: Bans minified JavaScript files based on a specified threshold.
- `ContentWhitelistPreValidator`: Returns true if the filename or content contains specific patterns.
- `FilenameWhitelistPreValidator`: Returns true if the filename matches an allow-listed name or extension.
- `FilenameBanlistPreValidator`: Returns false if the filename matches a ban-listed name, path, or extension.

## Post-Validation

Post-validators are critical in the secrets detection pipeline as they validate and filter the matches identified by the matchers. After the initial matches are identified, post-validators apply additional rules and checks to determine the legitimacy of the detected secrets. These validators ensure that the matches meet specific criteria, such as banning common false positives. They can also assess the entropy of the matches, verify the presence of a minimum number of digits, and apply various heuristics to filter out irrelevant matches. Post-validators provide an additional layer of validation and fine-tuning, improving the accuracy and reliability of the detected secrets by reducing the false positives rate and enhancing the overall effectiveness of the secrets detection engine.

The following post-validators are used by our secrets detection engine:

- `AssignmentBanlistPostValidator`: Discards matches based on the pattern of their assignment variables.
- `CommonHostBanlistPostValidator`: Bans commonly used false positive hosts.
- `CommonPasswordBanlistPostValidator`: Bans commonly used false positive passwords.
- `CommonUsernameBanlistPostValidator`: Bans commonly used false positive usernames.
- `CommonHighEntropyBanlistPostValidator`: Bans commonly used placeholder or generic high entropy values.
- `CommonValueBanlistPostValidator`: Bans commonly used false positive generic values.
- `DictFilterPostValidator`: Filters out matches that contain common dictionary words.
- `EntropyPostValidator`: Ensures that the entropy of the match is above a specified threshold.
- `HeuristicPostValidator`: Applies various heuristics to filter out certain types of matches.
- `MatchesPostValidator`: Applies post-validators to a subset of matches.
- `MinimumDigitsPostValidator`: Verifies that matches contain a minimum number of digits.
- `ValueBanlistPostValidator`: Bans matches that match specific value patterns.
- `ValueSimilarityPostValidator`: Bans match groups with a similarity above a specified threshold.
- `ContextWindowBanlistPostValidator`: Bans value patterns in a window around the matched string.

## Example

Let's consider the example of the [Slack App Token](detectors/specifics/slack_app_token.md) detector. It utilizes a `ContentWhitelistPreValidator` pre-validator which specifically looks for the prefix `xapp-` in the documents, which is a rare occurrence, appearing in only around one document per million on GitHub. As a result, the pre-validator quickly eliminates 99.9999% of the documents, significantly narrowing down the search.

Here are some examples of documents that would be accepted by the pre-validator:

```bash
curl -X POST https://slack.com/api/chat.postMessage \
  -d '{"channel":"C12345678","text":"Hello, Slack!"}' \
  -H "Content-Type: application/json"  \
  -H "Authorization: Bearer xapp-1-XQ1QRVG5098-91645510917198-7bda3ae63ec19bcbc94c9907a52835cd47f8835e0a7553ffa3a494a4bd82e572"
```

```text
bin/xfce4-set-wallpaper
include/xapp/libxapp/xapp-gtk-window.h
```

```python
SLACK_APP_TOKEN="xapp-1-ABCDEFGHIJK-12345678901234-aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
```

Among those documents, the matcher identifies two matches:

- `xapp-1-XQ1QRVG5098-91645510917198-7bda3ae63ec19bcbc94c9907a52835cd47f8835e0a7553ffa3a494a4bd82e572`
- `xapp-1-ABCDEFGHIJK-12345678901234-aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa`

However, the Slack App Token detector also employs an `EntropyPostValidator`, which filters out the second match due to its low entropy.

In conclusion, based on the example documents, the detector successfully identifies the only valid secret: `xapp-1-XQ1QRVG5098-91645510917198-7bda3ae63ec19bcbc94c9907a52835cd47f8835e0a7553ffa3a494a4bd82e572`.
