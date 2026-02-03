# Source: https://docs.sonarsource.com/sonarqube-community-build/extension-guide/developing-a-plugin/supporting-new-languages.md

# Source: https://docs.sonarsource.com/sonarqube-server/8.9/extension-guide/developing-a-plugin/supporting-new-languages.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.8/extension-guide/developing-a-plugin/supporting-new-languages.md

# Source: https://docs.sonarsource.com/sonarqube-server/9.9/extension-guide/developing-a-plugin/supporting-new-languages.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.0/extension-guide/developing-a-plugin/supporting-new-languages.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.1/extension-guide/developing-a-plugin/supporting-new-languages.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.2/extension-guide/developing-a-plugin/supporting-new-languages.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.3/extension-guide/developing-a-plugin/supporting-new-languages.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.4/extension-guide/developing-a-plugin/supporting-new-languages.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.5/extension-guide/developing-a-plugin/supporting-new-languages.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.6/extension-guide/developing-a-plugin/supporting-new-languages.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.7/extension-guide/developing-a-plugin/supporting-new-languages.md

# Source: https://docs.sonarsource.com/sonarqube-server/10.8/extension-guide/developing-a-plugin/supporting-new-languages.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/extension-guide/developing-a-plugin/supporting-new-languages.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/extension-guide/developing-a-plugin/supporting-new-languages.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/extension-guide/developing-a-plugin/supporting-new-languages.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/extension-guide/developing-a-plugin/supporting-new-languages.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/extension-guide/developing-a-plugin/supporting-new-languages.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/extension-guide/developing-a-plugin/supporting-new-languages.md

# Source: https://docs.sonarsource.com/sonarqube-server/extension-guide/developing-a-plugin/supporting-new-languages.md

# Supporting new languages

The steps to cover a new programming language are:

1. Write the grammar. This is the hardest part.
2. Write a parser (a parser simply parses an input based on your grammar to yield a parse tree).
3. Test your grammar, to ensure it is able to parse real-life language files.
4. Write a few parse tree visitors. Some visitors will compute metrics such as [executable-lines](https://docs.sonarsource.com/sonarqube-server/extension-guide/developing-a-plugin/executable-lines "mention"), while others will enforce [adding-coding-rules](https://docs.sonarsource.com/sonarqube-server/extension-guide/adding-coding-rules "mention"). A dozen or so visitors are sufficient for an initial release.
5. Write a scanner Sensor, in a SonarQube Server plugin, to launch the visitors.
6. Compute
   1. issues
   2. raw measures
   3. code duplications
   4. syntax highlighting
   5. symbol table
   6. coverage information (lines/branches to cover, line/branch hits)

In fulfilling these steps, the [Sonar Language Recognizer (SSLR)](https://github.com/SonarSource/sslr) can be an important resource.
