# Source: https://docs.socket.dev/docs/issues-list.md

# Alert Types Support

Which types of alerts are supported for which programming languages

export const targetEcosystems = [
  { 
    id: 'npm', 
    name: 'npm',
		icon: 'fab fa-npm text-[#CB3837]',
    supported: ['criticalCVE', 'cve', 'mediumCVE', 'mildCVE', 'malware', 'didYouMean', 'suspiciousStarActivity', 'gptMalware', 'gitDependency', 'gitHubDependency', 'httpDependency', 'obfuscatedFile', 'troll', 'telemetry', 'unstableOwnership', 'gptDidYouMean', 'gptSecurity', 'hasNativeCode', 'networkAccess', 'missingAuthor', 'potentialVulnerability', 'shellAccess', 'trivialPackage', 'usesEval', 'gptAnomaly', 'envVars', 'filesystemAccess', 'highEntropyStrings', 'newAuthor', 'urlStrings', 'unpopularPackage', 'minifiedFile', 'deprecated', 'unmaintained', 'explicitlyUnlicensedItem', 'licenseSpdxDisj', 'miscLicenseIssues', 'ambiguousClassifier', 'copyleftLicense', 'licenseException', 'noLicenseFound', 'nonpermissiveLicense', 'unidentifiedLicense', 'shrinkwrap', 'installScripts', 'manifestConfusion', 'debugAccess', 'dynamicRequire', 'badSemverDependency', 'floatingDependency'], 
    comingSoon: [] 
  },
  { 
    id: 'pypi', 
    name: 'PyPi',
    icon: 'fab fa-python text-[#3776AB]', // Official Blue
    supported: ['criticalCVE', 'cve', 'mediumCVE', 'mildCVE', 'malware', 'didYouMean', 'suspiciousStarActivity', 'gptMalware', 'obfuscatedFile', 'troll', 'telemetry', 'gptDidYouMean', 'gptSecurity', 'hasNativeCode', 'networkAccess', 'potentialVulnerability', 'shellAccess', 'usesEval', 'gptAnomaly', 'envVars', 'filesystemAccess', 'urlStrings', 'unpopularPackage', 'deprecated', 'unmaintained', 'explicitlyUnlicensedItem', 'licenseSpdxDisj', 'miscLicenseIssues', 'ambiguousClassifier', 'copyleftLicense', 'licenseException', 'noLicenseFound', 'nonpermissiveLicense', 'unidentifiedLicense'], 
    comingSoon: [] 
  },
  { 
    id: 'go', 
    name: 'Go Packages', 
    icon: 'fab fa-golang text-[#00ADD8]', // Official Blue
    supported: ['criticalCVE', 'cve', 'mediumCVE', 'mildCVE', 'malware', 'gptMalware', 'troll', 'telemetry', 'gptDidYouMean', 'gptSecurity', 'hasNativeCode', 'networkAccess', 'potentialVulnerability', 'shellAccess', 'usesEval', 'gptAnomaly', 'envVars', 'filesystemAccess', 'urlStrings', 'deprecated', 'explicitlyUnlicensedItem', 'licenseSpdxDisj', 'miscLicenseIssues', 'ambiguousClassifier', 'copyleftLicense', 'licenseException', 'noLicenseFound', 'nonpermissiveLicense', 'unidentifiedLicense'], 
    comingSoon: ['didYouMean', 'unpopularPackage', 'unmaintained'] 
  },
  { 
    id: 'maven', 
    name: 'Maven Central', 
    icon: 'fab fa-java text-[#5382A1]', // Java Blue
    supported: ['criticalCVE', 'cve', 'mediumCVE', 'mildCVE', 'malware', 'didYouMean', 'gptMalware', 'troll', 'telemetry', 'gptDidYouMean', 'gptSecurity', 'hasNativeCode', 'networkAccess', 'potentialVulnerability', 'shellAccess', 'usesEval', 'gptAnomaly', 'envVars', 'filesystemAccess', 'urlStrings', 'unmaintained', 'explicitlyUnlicensedItem', 'licenseSpdxDisj', 'miscLicenseIssues', 'ambiguousClassifier', 'copyleftLicense', 'licenseException', 'noLicenseFound', 'nonpermissiveLicense', 'unidentifiedLicense'], 
    comingSoon: [] 
  },
  { 
    id: 'ruby', 
    name: 'RubyGems',
    icon: 'fas fa-gem text-[#E9573F]', // Gem Red
    supported: ['criticalCVE', 'cve', 'mediumCVE', 'mildCVE', 'malware', 'gptMalware', 'troll', 'telemetry', 'gptDidYouMean', 'gptSecurity', 'hasNativeCode', 'networkAccess', 'potentialVulnerability', 'shellAccess', 'usesEval', 'gptAnomaly', 'envVars', 'filesystemAccess', 'urlStrings', 'unpopularPackage', 'unmaintained', 'explicitlyUnlicensedItem', 'licenseSpdxDisj', 'miscLicenseIssues', 'ambiguousClassifier', 'copyleftLicense', 'licenseException', 'noLicenseFound', 'nonpermissiveLicense', 'unidentifiedLicense'], 
    comingSoon: ['didYouMean'] 
  },
  { 
    id: 'nuget', 
    name: 'NuGet', 
    icon: 'fab fa-microsoft text-[#004880]', // Microsoft Blue
    supported: ['criticalCVE', 'cve', 'mediumCVE', 'mildCVE', 'malware', 'didYouMean', 'gptMalware', 'troll', 'telemetry', 'gptDidYouMean', 'gptSecurity', 'hasNativeCode', 'networkAccess', 'potentialVulnerability', 'shellAccess', 'usesEval', 'gptAnomaly', 'envVars', 'filesystemAccess', 'unpopularPackage', 'explicitlyUnlicensedItem', 'licenseSpdxDisj', 'miscLicenseIssues', 'ambiguousClassifier', 'copyleftLicense', 'licenseException', 'noLicenseFound', 'nonpermissiveLicense', 'unidentifiedLicense'], 
    comingSoon: [] 
  },
  { 
    id: 'crates', 
    name: 'Crates', 
    icon: 'fab fa-rust text-[#000000] dark:text-white', // Rust Standard
    supported: ['criticalCVE', 'cve', 'mediumCVE', 'mildCVE', 'malware', 'didYouMean', 'gptMalware', 'troll', 'telemetry', 'gptDidYouMean', 'gptSecurity', 'hasNativeCode', 'networkAccess', 'potentialVulnerability', 'shellAccess', 'usesEval', 'gptAnomaly', 'envVars', 'filesystemAccess', 'unpopularPackage', 'explicitlyUnlicensedItem', 'licenseSpdxDisj', 'miscLicenseIssues', 'ambiguousClassifier', 'copyleftLicense', 'licenseException', 'noLicenseFound', 'nonpermissiveLicense', 'unidentifiedLicense'], 
    comingSoon: [] 
  },
  { 
    id: 'huggingface', 
    name: 'Hugging Face', 
    icon: 'fas fa-face-smiling-hands text-[#FFD21E]', // AI/Hugging Face Yellow
    supported: ['criticalCVE', 'cve', 'mediumCVE', 'mildCVE', 'malware', 'didYouMean', 'gptMalware', 'troll', 'telemetry', 'gptDidYouMean', 'gptSecurity', 'hasNativeCode', 'networkAccess', 'shellAccess', 'usesEval', 'gptAnomaly', 'envVars', 'filesystemAccess', 'unpopularPackage', 'explicitlyUnlicensedItem', 'licenseSpdxDisj', 'miscLicenseIssues', 'ambiguousClassifier', 'copyleftLicense', 'licenseException', 'noLicenseFound', 'nonpermissiveLicense', 'unidentifiedLicense'], 
    comingSoon: [] 
  },
  { 
    id: 'actions', 
    name: 'Github Actions', 
    icon: 'fab fa-github text-[#24292e] dark:text-white', // GitHub Black/White
    supported: ['malware', 'didYouMean', 'gptMalware', 'obfuscatedFile', 'troll', 'telemetry', 'gptSecurity', 'hasNativeCode', 'networkAccess', 'potentialVulnerability', 'shellAccess', 'trivialPackage', 'usesEval', 'gptAnomaly', 'envVars', 'filesystemAccess', 'highEntropyStrings', 'urlStrings', 'minifiedFile', 'explicitlyUnlicensedItem', 'licenseSpdxDisj', 'miscLicenseIssues', 'ambiguousClassifier', 'copyleftLicense', 'licenseException', 'noLicenseFound', 'nonpermissiveLicense', 'unidentifiedLicense'], 
    comingSoon: ['criticalCVE', 'cve', 'mediumCVE', 'mildCVE', 'unstableOwnership', 'gptDidYouMean', 'missingAuthor', 'deprecated', 'unmaintained'] 
  },
  { 
    id: 'openvsx', 
    name: 'OpenVSX', 
    icon: 'fas fa-code text-[#007ACC]', // VS Code Blue
    supported: ['malware', 'gptMalware', 'obfuscatedFile', 'troll', 'telemetry', 'gptSecurity', 'hasNativeCode', 'networkAccess', 'potentialVulnerability', 'shellAccess', 'usesEval', 'gptAnomaly', 'envVars', 'filesystemAccess', 'highEntropyStrings', 'urlStrings', 'deprecated'], 
    comingSoon: ['didYouMean', 'gitDependency', 'gitHubDependency', 'httpDependency', 'unstableOwnership', 'gptDidYouMean', 'newAuthor', 'unpopularPackage', 'minifiedFile', 'unmaintained'] 
  },
  { 
    id: 'chrome', 
    name: 'Chrome', 
    icon: 'fab fa-chrome text-[#4285F4]', // Google Blue (or could use green/yellow/red)
    supported: ['gptMalware', 'troll', 'telemetry', 'gptSecurity', 'gptAnomaly'], 
    comingSoon: [] 
  },
  { 
    id: 'swift', 
    name: 'Swift', 
    icon: 'fab fa-swift text-[#F05138]', // Swift Orange
    supported: ['criticalCVE', 'cve', 'mediumCVE', 'mildCVE'], 
    comingSoon: [] 
  },
  { 
    id: 'conan', 
    name: 'Conan Center', 
    icon: 'fas fa-frog text-[#6699CB]', // C++ / JFrog Blue
    supported: ['criticalCVE', 'cve', 'mediumCVE', 'mildCVE'], 
    comingSoon: [] 
  },
  { 
    id: 'julia', 
    name: 'Julia', 
    icon: 'fas fa-circle-nodes text-[#9558B2]', // Julia Purple
    supported: ['criticalCVE', 'cve', 'mediumCVE', 'mildCVE'], 
    comingSoon: [] 
  },
  { 
    id: 'pub', 
    name: 'Pub', 
    icon: 'fab fa-dart-lang text-[#0175C2]', // Dart Blue
    supported: ['criticalCVE', 'cve', 'mediumCVE', 'mildCVE'], 
    comingSoon: [] 
  },
  { 
    id: 'hex', 
    name: 'Hex', 
    icon: 'fab fa-erlang text-[#ec485b]', // Erlang pink
    supported: ['criticalCVE', 'cve', 'mediumCVE', 'mildCVE'], 
    comingSoon: [] 
  },
  { 
    id: 'cocoapods', 
    name: 'CocoaPods', 
    icon: 'fab fa-apple text-[#EA524F]', // CocoaPods Red
    supported: ['criticalCVE', 'cve', 'mediumCVE', 'mildCVE'], 
    comingSoon: []
   }
]

export const alertsData = [
  {
    category: "Vulnerability",
    alerts: [
      { name: "Critical CVE", 
        severity: "Critical", 
        slug: "criticalCVE" 
      },
      { name: "High CVE", 
        severity: "High", 
        slug: "cve" 
      },
      { name: "Medium CVE", 
        severity: "Medium", 
        slug: "mediumCVE" 
      },
      { name: "Low CVE", 
        severity: "Low", 
        slug: "mildCVE"
       }
    ]
  },
  {
    category: "Supply Chain Risk",
    alerts: [
      { name: "Known Malware", 
        severity: "Critical", 
        slug: "malware" 
      },
      { name: "Possible typosquat attack", 
        severity: "Critical", 
        slug: "didYouMean" 
      },
      { name: "Suspicious Stars on GitHub", 
        severity: "High", 
        slug: "suspiciousStarActivity" 
      },
      { name: "AI-detected potential malware", 
        severity: "High", 
        slug: "gptMalware" 
      },
      { name: "Git dependency", 
        severity: "High", 
        slug: "gitDependency" 
      },
      { name: "GitHub dependency", 
        severity: "High", 
        slug: "gitHubDependency" 
      },
      { name: "HTTP dependency", 
        severity: "High", 
        slug: "httpDependency" 
      },
      { name: "Obfuscated code", 
        severity: "High", 
        slug: "obfuscatedFile" 
      },
      { name: "Protestware/unwanted behavior", 
        severity: "High", 
        slug: "troll" 
      },
      { name: "Telemetry", 
        severity: "High", 
        slug: "telemetry" 
      },
      { name: "Unstable ownership", 
        severity: "High", 
        slug: "unstableOwnership" 
      },
      { name: "AI-detected possible typosquat", 
        severity: "Medium", 
        slug: "gptDidYouMean" 
      },
      { name: "AI-detected potential security risk", 
        severity: "Medium", 
        slug: "gptSecurity" 
      },
      { name: "Native code", 
        severity: "Medium", 
        slug: "hasNativeCode" 
      },
      { name: "Network access", 
        severity: "Medium", 
        slug: "networkAccess" 
      },
      { name: "Non-existent author", 
        severity: "Medium", 
        slug: "missingAuthor" 
      },
      { name: "Potential vulnerability", 
        severity: "Medium", 
        slug: "potentialVulnerability" 
      },
      { name: "Shell access", 
        severity: "Medium", 
        slug: "shellAccess" 
      },
      { name: "Trivial Package", 
        severity: "Medium", 
        slug: "trivialPackage" 
      },
      { name: "Uses eval", 
        severity: "Medium", 
        slug: "usesEval" 
      },
      { name: "AI-detected potential code anomaly", 
        severity: "Low", 
        slug: "gptAnomaly" 
      },
      { name: "Environment variable access", 
        severity: "Low", 
        slug: "envVars" 
      },
      { name: "Filesystem access", 
        severity: "Low", 
        slug: "filesystemAccess" 
      },
      { name: "High entropy strings", 
        severity: "Low", 
        slug: "highEntropyStrings" 
      },
      { name: "New author", 
        severity: "Low", 
        slug: "newAuthor" 
      },
      { name: "URL strings", 
        severity: "Low", 
        slug: "urlStrings" 
      },
      { name: "NPM Shrinkwrap", 
        severity: "High", 
        slug: "shrinkwrap" 
      },
      { name: "Install scripts", 
        severity: "Medium", 
        slug: "installScripts" 
      },
      { name: "Manifest confusion", 
        severity: "Medium", 
        slug: "manifestConfusion" 
      },
      { name: "Debug access", 
        severity: "Low", 
        slug: "debugAccess" 
      },
      { name: "Dynamic require", 
        severity: "Low", 
        slug: "dynamicRequire"
       }
    ]
  },
  {
    category: "Quality",
    alerts: [
      { name: "Unpopular package", 
        severity: "Medium", 
        slug: "unpopularPackage" 
      },
      { name: "Minified code", 
        severity: "Low", 
        slug: "minifiedFile" 
      },
      { name: "Bad dependency semver", 
        severity: "Medium", 
        slug: "badSemverDependency" 
      },
      { name: "Wildcard dependency", 
        severity: "Medium", 
        slug: "floatingDependency"
       }
    ]
  },
  {
    category: "Maintenance",
    alerts: [
      { name: "Deprecated", 
        severity: "Medium", 
        slug: "deprecated" 
      },
      { name: "Unmaintained", 
        severity: "Low", 
        slug: "unmaintained"
       }
    ]
  },
  {
    category: "License",
    alerts: [
      { name: "Explicitly Unlicensed Item", 
        severity: "High", 
        slug: "explicitlyUnlicensedItem" 
      },
      { name: "License Policy Violation", 
        severity: "High", 
        slug: "licenseSpdxDisj" 
      },
      { name: "Misc. License Issues", 
        severity: "Medium", 
        slug: "miscLicenseIssues" 
      },
      { name: "Ambiguous License Classifier", 
        severity: "Low", 
        slug: "ambiguousClassifier" 
      },
      { name: "Copyleft License", 
        severity: "Low", 
        slug: "copyleftLicense" 
      },
      { name: "License exception", 
        severity: "Low", 
        slug: "licenseException" 
      },
      { name: "No License Found", 
        severity: "Low", 
        slug: "noLicenseFound" 
      },
      { name: "Non-permissive License", 
        severity: "Low", 
        slug: "nonpermissiveLicense" 
      },
      { name: "Unidentified License", 
        severity: "Low", 
        slug: "unidentifiedLicense"
       }
    ]
  }
]

<AlertTable ecosystems={targetEcosystems} data={alertsData} />