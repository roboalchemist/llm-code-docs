# Source: https://github.com/eslint-community/eslint-plugin-security/blob/main/docs/rules/detect-disable-mustache-escape.md

# Detects "object.escapeMarkup = false", which can be used with some template engines to disable escaping of HTML entities (`security/detect-disable-mustache-escape`)

⚠️ This rule _warns_ in the ✅ `recommended` config.

<!-- end auto-generated rule header -->

This can lead to Cross-Site Scripting (XSS) vulnerabilities.

More information: [OWASP XSS](<https://www.owasp.org/index.php/Cross-site_Scripting_(XSS)>)
