# Source: https://iterm2.com/documentation-search-syntax.html

[Table of Contents](#)

Introduction

- [Highlights for New Users](https://iterm2.com/documentation-highlights.html)

- [General Usage](https://iterm2.com/documentation-general-usage.html)

User Interface

- [Menu Items](https://iterm2.com/documentation-menu-items.html)

- [Settings](https://iterm2.com/documentation-preferences.html)

- [Touch Bar](https://iterm2.com/documentation-touch-bar.html)

- [Copy Mode](https://iterm2.com/documentation-copymode.html)

- [Fonts](https://iterm2.com/documentation-fonts.html)

- [Profile Search Syntax](https://iterm2.com/documentation-search-syntax.html)

- [Command Selection and Command URLs](https://iterm2.com/documentation-command-selection.html)

- [Status Bar](https://iterm2.com/documentation-status-bar.html)

Features

- [Automatic Profile Switching](https://iterm2.com/documentation-automatic-profile-switching.html)

- [Badges](https://iterm2.com/documentation-badges.html)

- [Buried Sessions](https://iterm2.com/documentation-buried-sessions.html)

- [Captured Output](https://iterm2.com/documentation-captured-output.html)

- [Coprocesses](https://iterm2.com/documentation-coprocesses.html)

- [Hotkeys](https://iterm2.com/documentation-hotkey.html)

- [Session Restoration](https://iterm2.com/documentation-restoration.html)

- [Shell Integration](https://iterm2.com/documentation-shell-integration.html)

- [Smart Selection](https://iterm2.com/documentation-smart-selection.html)

- [tmux Integration](https://iterm2.com/documentation-tmux-integration.html)

- [Triggers](https://iterm2.com/documentation-triggers.html)

- [Utilities](https://iterm2.com/documentation-utilities.html)

- [Web Browser](https://iterm2.com/documentation-web.html)

- [AI Chat](https://iterm2.com/documentation-ai-chat.html)

Scripting

- [Scripting Fundamentals](https://iterm2.com/documentation-scripting-fundamentals.html)

- [Scripting Variables](https://iterm2.com/documentation-variables.html)

- [Python API](https://iterm2.com/python-api)

- [Scripting with AppleScript (Deprecated)](https://iterm2.com/documentation-scripting.html)

Advanced

- [Dynamic Profiles](https://iterm2.com/documentation-dynamic-profiles.html)

- [Inline Images Protocol](https://iterm2.com/documentation-images.html)

- [Proprietary Escape Codes](https://iterm2.com/documentation-escape-codes.html)

# Search Syntax

When iTerm2 presents a list of profiles, it usually includes a search box. The search box uses a special syntax that lets you tailor your searches to quickly find what you're looking for.

### Searching Profiles

Each word in the search query must match at least one word in either the title or the tags of a profile in order for that profile to be matched by the query. For a word to be a match, it must be a substring.

    Query
     &nbsp  
    Profile Name
      
    Matches?

    Linux
        
    **Linux**
      
    Yes

    x
        
    Linu**x**
      
    Yes

    z
        
    Linux
      
    No

    George L
        
    **George**'s **L**inux Machine
      
    Yes

### Operators

You may prefix a phrase in the search query with an *operator* to narrow your query. These operators are defined:

- The *name:* operator only tries to match words in the profile's name.

- The *tag:* operator only tries to match words in the profile's tags.

- The *command:* operator only tries to match words in the profile's command. Note that the command is only searched for words that explicitly use the `command` operator. Available in iTerm2 version 3.5.5 and later.

### Quoting

You can require that two or more words occur in order by putting quotes in your query. For example:

    Query
        
    Profile Name
    Matches?

    "Linux machine"
        
    George's **Linux machine**
    Yes

    "machine Linux"
        
    Linux machine
    No

### Anchoring

Normally, words in a query must match a substring of a word in the title or tags of a profile. You can require that a word in your query matches a prefix of a word in the title or tags by inserting a caret (^) before the word. You can require that a word in your query matches the suffix of a word in the title or tags by appending a dollar sign ($) after the word. For example, the query *^a* matches only profiles with words starting with "a". The query *a$* matches words ending in "a". The query *^a$* matches only the word "a".

    Query
     &nbsp  
    Profile Name
    Matches?

    ^root
        
    [[email&#160;protected]](https://iterm2.com/cdn-cgi/l/email-protection)
    Yes

    ^root
        
    Groot!
    No

    root$
        
    Groot
    Yes

    ^root$
        
    Groot
    No

    ^root$
        
    root
    Yes

### Combining Features

You may combine quoting, operators, and anchors. The operator always comes first, followed by a caret, followed by a quoted string, followed by a dollar sign. Consider the following examples:

```
name:^"George's Linux Machine"$
```

Three consecutive whole words in the profile's name must equal "George's Linux Machine".

```
name:"George's Linux Machine"$
```

Would match a profile named "XGeorge's Linux Machine", unlike the previous example.

```
name:^"George's Linux Machine"
```

Would match a profile named "George's Linux MachineX", unlike the first example.

```
name:"George's Linux Machine"
```

Would match a profile named "XGeorge's Linux MachineX", unlike the first example.

```
name:^George's
name:George's$
name:^George's$

```

A word having the prefix, suffix, or exactly matching "George's" must occur in the profile's name to match these queries, respectively.