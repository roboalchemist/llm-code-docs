# Source: https://docs.sonarsource.com/sonarqube-server/2025.2/user-guide/rules/rules-for-ai-codefix.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.3/user-guide/rules/rules-for-ai-codefix.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.5/user-guide/rules/rules-for-ai-codefix.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.1/user-guide/rules/rules-for-ai-codefix.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.4/user-guide/rules/rules-for-ai-codefix.md

# Source: https://docs.sonarsource.com/sonarqube-server/2025.6/user-guide/rules/rules-for-ai-codefix.md

# Source: https://docs.sonarsource.com/sonarqube-server/user-guide/rules/rules-for-ai-codefix.md

# Source: https://docs.sonarsource.com/sonarqube-cloud/digging-deeper/rules-for-ai-codefix.md

# Rules for AI CodeFix

*AI features are only available in SonarQube Cloud Team and Enterprise plans*. See the [subscription-plans](https://docs.sonarsource.com/sonarqube-cloud/administering-sonarcloud/managing-subscription/subscription-plans "mention") page for more detail&#x73;*.*

In SonarQube, analyzers contribute rules executed on source code to generate issues. Some of these rules are more complex than others and therefore, not suitable for use with the [ai-codefix](https://docs.sonarsource.com/sonarqube-cloud/ai-capabilities/ai-codefix "mention"). This page lists rules that work with the AI CodeFix service.

### Rules covered with AI CodeFix <a href="#ai-codefix-rules" id="ai-codefix-rules"></a>

Below you’ll find a list of Sonar Rules that are eligible for use with our AI CodeFix feature. We’ve tested each of these rules in the supported AI models and given them a confidence score to ensure they can effectively help you resolve issues. Once a rule passes our certification, it’s added to the AI CodeFix service and becomes available to you. We’re constantly working to expand this list by evaluating more rules and enhancing our AI capabilities.

Each collapsible holds a list of rules for the listed language. You will find instructions inside on how to find the detailed rule description on the [Sonar Rules website](https://rules.sonarsource.com/).

<details>

<summary>AI CodeFix rules for C++</summary>

**AI CodeFix rules for C++**

Go to the [Sonar Rules website](https://rules.sonarsource.com/) to search for more information about your rule.

* select any rule at <https://rules.sonarsource.com/cpp/>
* replace the RSPEC number in the rule’s URL with the relevant rule number listed below.

For example, to read about rule `cpp:S1048`, go to <https://rules.sonarsource.com/cpp/RSPEC-1048/>

cpp:S1048

cpp:S1051

cpp:S1052

cpp:S1065

cpp:S1066

cpp:S1079

cpp:S1110

cpp:S1117

cpp:S1121

cpp:S1131

cpp:S1155

cpp:S117

cpp:S1172

cpp:S1188

cpp:S1199

cpp:S1235

cpp:S1238

cpp:S125

cpp:S1264

cpp:S1270

cpp:S1271

cpp:S1301

cpp:S134

cpp:S1481

cpp:S1669

cpp:S1705

cpp:S1751

cpp:S1764

cpp:S1768

cpp:S1772

cpp:S1854

cpp:S1905

cpp:S1912

cpp:S1915

cpp:S1916

cpp:S2259

cpp:S2275

cpp:S2305

cpp:S2343

cpp:S2681

cpp:S2807

cpp:S3229

cpp:S3358

cpp:S3458

cpp:S3490

cpp:S3539

cpp:S3542

cpp:S3549

cpp:S3574

cpp:S3659

cpp:S3806

cpp:S3923

cpp:S3972

cpp:S3973

cpp:S4334

cpp:S4962

cpp:S5028

cpp:S5271

cpp:S5303

cpp:S5319

cpp:S5350

cpp:S5416

cpp:S5523

cpp:S5536

cpp:S5566

cpp:S5817

cpp:S5820

cpp:S5825

cpp:S5827

cpp:S5946

cpp:S5951

cpp:S5997

cpp:S6005

cpp:S6024

cpp:S6045

cpp:S6164

cpp:S6171

cpp:S6178

cpp:S6180

cpp:S6185

cpp:S6186

cpp:S6195

cpp:S6197

cpp:S6226

cpp:S6229

cpp:S6230

cpp:S6234

cpp:S6391

cpp:S7034

cpp:S7116

cpp:S811

cpp:S818

cpp:S831

cpp:S834

cpp:S835

cpp:S836

cpp:S864

cpp:S868

cpp:S871

cpp:S872

cpp:S878

cpp:S905

cpp:S959

cpp:S963

cpp:S966

cpp:S982

cpp:S991

cpp:S994

cpp:S995

cpp:S998

</details>

<details>

<summary>AI CodeFix rules for C# and Roslyn security</summary>

**AI CodeFix rules for C#**

Go to the [Sonar Rules website](https://rules.sonarsource.com/) to search for more information about your rule.

* select any rule at <https://rules.sonarsource.com/csharp/>
* replace the RSPEC number in the rule’s URL with the relevant rule number listed below.

For example, to read about rule `csharpsquid:S100`, go to <https://rules.sonarsource.com/csharp/RSPEC-100/>

csharpsquid:S100

csharpsquid:S101

csharpsquid:S1066

csharpsquid:S107

csharpsquid:S1110

csharpsquid:S1116

csharpsquid:S1117

csharpsquid:S1118

csharpsquid:S112

csharpsquid:S1121

csharpsquid:S1125

csharpsquid:S1128

csharpsquid:S1135

csharpsquid:S1144

csharpsquid:S1155

csharpsquid:S1168

csharpsquid:S1172

csharpsquid:S1186

csharpsquid:S1199

csharpsquid:S121

csharpsquid:S1244

csharpsquid:S125

csharpsquid:S1264

csharpsquid:S1450

csharpsquid:S1481

csharpsquid:S1643

csharpsquid:S1656

csharpsquid:S1659

csharpsquid:S1764

csharpsquid:S1848

csharpsquid:S1854

csharpsquid:S1871

csharpsquid:S1905

csharpsquid:S1939

csharpsquid:S1940

csharpsquid:S2178

csharpsquid:S2219

csharpsquid:S2223

csharpsquid:S2259

csharpsquid:S2292

csharpsquid:S2325

csharpsquid:S2342

csharpsquid:S2344

csharpsquid:S2368

csharpsquid:S2372

csharpsquid:S2376

csharpsquid:S2386

csharpsquid:S2445

csharpsquid:S2479

csharpsquid:S2583

csharpsquid:S2629

csharpsquid:S2681

csharpsquid:S2701

csharpsquid:S2933

csharpsquid:S2971

csharpsquid:S3010

csharpsquid:S3052

csharpsquid:S3217

csharpsquid:S3218

csharpsquid:S3220

csharpsquid:S3241

csharpsquid:S3242

csharpsquid:S3247

csharpsquid:S3257

csharpsquid:S3260

csharpsquid:S3267

csharpsquid:S3353

csharpsquid:S3358

csharpsquid:S3415

csharpsquid:S3442

csharpsquid:S3445

csharpsquid:S3456

csharpsquid:S3457

csharpsquid:S3604

csharpsquid:S3626

csharpsquid:S3655

csharpsquid:S3878

csharpsquid:S3881

csharpsquid:S3897

csharpsquid:S3903

csharpsquid:S3928

csharpsquid:S3949

csharpsquid:S3973

csharpsquid:S4035

csharpsquid:S4050

csharpsquid:S4056

csharpsquid:S4058

csharpsquid:S4275

csharpsquid:S4487

csharpsquid:S4581

csharpsquid:S4663

csharpsquid:S6602

csharpsquid:S6603

csharpsquid:S6605

csharpsquid:S6608

csharpsquid:S6667

csharpsquid:S6668

csharpsquid:S6672

csharpsquid:S6678

csharpsquid:S6966

csharpsquid:S927

**AI CodeFix rules for Roslyn rules**

Go to the [Sonar Rules website](https://rules.sonarsource.com/) to search for more information about your rule.

* select any rule at <https://rules.sonarsource.com/csharp/>
* replace the RSPEC number in the rule’s URL with the relevant rule number listed below.

For example, to read about rule `roslyn.sonaranalyzer.security.cs:S2076`, go to <https://rules.sonarsource.com/csharp/RSPEC-2076/>

roslyn.sonaranalyzer.security.cs:S2076

roslyn.sonaranalyzer.security.cs:S2078

roslyn.sonaranalyzer.security.cs:S2091

roslyn.sonaranalyzer.security.cs:S3649

roslyn.sonaranalyzer.security.cs:S5131

roslyn.sonaranalyzer.security.cs:S5145

roslyn.sonaranalyzer.security.cs:S5146

roslyn.sonaranalyzer.security.cs:S5334

roslyn.sonaranalyzer.security.cs:S6096

roslyn.sonaranalyzer.security.cs:S6173

roslyn.sonaranalyzer.security.cs:S6639

roslyn.sonaranalyzer.security.cs:S6641

</details>

<details>

<summary>AI CodeFix rules for Java and Java security</summary>

**AI CodeFix rules for Java**

Go to the [Sonar Rules website](https://rules.sonarsource.com/) to search for more information about your rule.

* select any rule at <https://rules.sonarsource.com/java/>
* replace the RSPEC number in the rule’s URL with the relevant rule number listed below.

For example, to read about rule `java:S100`, go to <https://rules.sonarsource.com/java/RSPEC-100/>

java:S100

java:S101

java:S1065

java:S1068

java:S108

java:S1104

java:S1110

java:S1116

java:S1117

java:S1118

java:S1121

java:S1124

java:S1125

java:S1126

java:S1128

java:S1130

java:S1132

java:S1135

java:S1144

java:S1149

java:S115

java:S116

java:S1168

java:S1155

java:S1157

java:S117

java:S1170

java:S1171

java:S1172

java:S1181

java:S1182

java:S1186

java:S119

java:S1192

java:S1197

java:S120

java:S1206

java:S1210

java:S1221

java:S1223

java:S1244

java:S125

java:S1264

java:S1301

java:S131

java:S1319

java:S135

java:S1444

java:S1450

java:S1481

java:S1488

java:S1602

java:S1604

java:S1611

java:S1612

java:S1643

java:S1656

java:S1659

java:S1764

java:S1845

java:S1854

java:S1858

java:S1871

java:S1905

java:S1940

java:S1994

java:S2039

java:S2047

java:S2094

java:S2129

java:S2130

java:S2140

java:S2148

java:S2153

java:S2162

java:S2164

java:S2178

java:S2184

java:S2185

java:S2189

java:S2200

java:S2201

java:S2209

java:S2211

java:S2251

java:S2252

java:S2259

java:S2293

java:S2325

java:S2326

java:S2333

java:S2386

java:S2440

java:S2479

java:S2589

java:S2681

java:S2694

java:S2701

java:S2786

java:S2864

java:S2974

java:S3008

java:S3012

java:S3052

java:S3358

java:S3400

java:S3457

java:S3518

java:S3626

java:S3740

java:S3776

java:S3923

java:S3973

java:S3985

java:S4144

java:S4165

java:S4274

java:S4838

java:S4973

java:S5361

java:S5411

java:S5738

java:S5867

java:S6208

java:S6213

java:S7158

java:S818

java:S881

**AI CodeFix rules for Java security**

Go to the [Sonar Rules website](https://rules.sonarsource.com/) to search for more information about your rule.

* select any rule at <https://rules.sonarsource.com/java/>
* replace the RSPEC number in the rule’s URL with the relevant rule number listed below.

For example, to read about rule `javasecurity:S2076`, go to <https://rules.sonarsource.com/java/RSPEC-2076/>

javasecurity:S2076

javasecurity:S2078

javasecurity:S2083

javasecurity:S2091

javasecurity:S2631

javasecurity:S3649

javasecurity:S5131

javasecurity:S5145

javasecurity:S5146

javasecurity:S5167

javasecurity:S5883

javasecurity:S6173

javasecurity:S6547

javasecurity:S6549

</details>

<details>

<summary>AI CodeFix rules for JavaScript and JavaScript security</summary>

**AI CodeFix rules for JavaScript**

Go to the [Sonar Rules website](https://rules.sonarsource.com/) to search for more information about your rule.

* select any rule at <https://rules.sonarsource.com/javascript/>
* replace the RSPEC number in the rule’s URL with the relevant rule number listed below.

For example, to read about rule `javascript:S100`, go to <https://rules.sonarsource.com/javascript/RSPEC-100/>

javascript:S100

javascript:S101

javascript:S1066

javascript:S108

javascript:S1082

javascript:S1105

javascript:S1117

javascript:S1121

javascript:S1125

javascript:S1126

javascript:S113

javascript:S1131

javascript:S117

javascript:S1172

javascript:S1186

javascript:S1199

javascript:S121

javascript:S125

javascript:S126

javascript:S1264

javascript:S1438

javascript:S1440

javascript:S1441

javascript:S1481

javascript:S1533

javascript:S1534

javascript:S1539

javascript:S1656

javascript:S1751

javascript:S1763

javascript:S1764

javascript:S1788

javascript:S1854

javascript:S1871

javascript:S1874

javascript:S1940

javascript:S1994

javascript:S2094

javascript:S2137

javascript:S2427

javascript:S2430

javascript:S2681

javascript:S2703

javascript:S2814

javascript:S2871

javascript:S3353

javascript:S3358

javascript:S3403

javascript:S3504

javascript:S3512

javascript:S3514

javascript:S3516

javascript:S3524

javascript:S3579

javascript:S3626

javascript:S3696

javascript:S3699

javascript:S3760

javascript:S3782

javascript:S3800

javascript:S3801

javascript:S3972

javascript:S3973

javascript:S4138

javascript:S4144

javascript:S6509

javascript:S6557

javascript:S6582

javascript:S6594

javascript:S6638

javascript:S6643

javascript:S6644

javascript:S6645

javascript:S6647

javascript:S6661

javascript:S6666

javascript:S6836

javascript:S6959

javascript:S878

javascript:S881

javascript:S905

javascript:S909

javascript:S930

**AI CodeFix rules for JS security**

Go to the [Sonar Rules website](https://rules.sonarsource.com/) to search for more information about your rule.

* select any rule at <https://rules.sonarsource.com/javascript/>
* replace the RSPEC number in the rule’s URL with the relevant rule number listed below.

For example, to read about rule `jssecurity:S2083`, go to <https://rules.sonarsource.com/javascript/RSPEC-2083/>

jssecurity:S2083

jssecurity:S2631

jssecurity:S3649

jssecurity:S5131

jssecurity:S5146

jssecurity:S5696

jssecurity:S6096

</details>

<details>

<summary>AI CodeFix rules for Python and Python security</summary>

**AI CodeFix rules for Python**

Go to the [Sonar Rules website](https://rules.sonarsource.com/) to search for more information about your rule.

* select any rule at <https://rules.sonarsource.com/python/>
* replace the RSPEC number in the rule’s URL with the relevant rule number listed below.

For example, to read about rule `python:S100`, go to <https://rules.sonarsource.com/python/RSPEC-100/>

python:S100

python:S101

python:S1066

python:S108

python:S1110

python:S112

python:S1128

python:S1142

python:S117

python:S1172

python:S1186

python:S1244

python:S125

python:S1481

python:S1515

python:S1542

python:S1720

python:S1721

python:S1722

python:S1854

python:S1871

python:S1940

python:S2772

python:S2836

python:S3457

python:S3626

python:S3801

python:S5603

python:S5717

python:S5754

python:S5795

python:S5799

python:S5806

python:S5890

python:S5906

python:S6538

python:S6660

python:S6711

python:S6903

**AI CodeFix rules for Python security**

Go to the [Sonar Rules website](https://rules.sonarsource.com/) to search for more information about your rule.

* select any rule at <https://rules.sonarsource.com/python/>
* replace the RSPEC number in the rule’s URL with the relevant rule number listed below.

For example, to read about rule `pythonsecurity:S2076`, go to <https://rules.sonarsource.com/python/RSPEC-2076/>

pythonsecurity:S2076

pythonsecurity:S2078

pythonsecurity:S2083

pythonsecurity:S3649

pythonsecurity:S5131

pythonsecurity:S5144

pythonsecurity:S5145

pythonsecurity:S5146

pythonsecurity:S5167

pythonsecurity:S5334

</details>

<details>

<summary>AI CodeFix rules for TypeScript and TypeScript security</summary>

**AI CodeFix rules for TypeScript**

Go to the [Sonar Rules website](https://rules.sonarsource.com/) to search for more information about your rule.

* select any rule at <https://rules.sonarsource.com/typescript/>
* replace the RSPEC number in the rule’s URL with the relevant rule number listed below.

For example, to read about rule `typescript:S100`, go to <https://rules.sonarsource.com/typescript/RSPEC-100/>

typescript:S100

typescript:S101

typescript:S1066

typescript:S108

typescript:S1082

typescript:S1105

typescript:S1117

typescript:S1121

typescript:S1125

typescript:S113

typescript:S1131

typescript:S117

typescript:S1172

typescript:S1186

typescript:S1199

typescript:S121

typescript:S125

typescript:S126

typescript:S1264

typescript:S1438

typescript:S1440

typescript:S1441

typescript:S1533

typescript:S1539

typescript:S1656

typescript:S1751

typescript:S1763

typescript:S1764

typescript:S1788

typescript:S1854

typescript:S1871

typescript:S1874

typescript:S1940

typescript:S1994

typescript:S2094

typescript:S2137

typescript:S2427

typescript:S2430

typescript:S2681

typescript:S2871

typescript:S3353

typescript:S3358

typescript:S3504

typescript:S3512

typescript:S3514

typescript:S3516

typescript:S3524

typescript:S3579

typescript:S3626

typescript:S3696

typescript:S3699

typescript:S3972

typescript:S4138

typescript:S4144

typescript:S4325

typescript:S6509

typescript:S6557

typescript:S6564

typescript:S6582

typescript:S6594

typescript:S6638

typescript:S6643

typescript:S6644

typescript:S6647

typescript:S6661

typescript:S6666

typescript:S6836

typescript:S6959

typescript:S878

typescript:S881

typescript:S905

**AI CodeFix rules for TypeScript security**

Go to the [Sonar Rules website](https://rules.sonarsource.com/) to search for more information about your rule.

* select any rule at <https://rules.sonarsource.com/typescript/>
* replace the RSPEC number in the rule’s URL with the relevant rule number listed below.

For example, to read about rule `tssecurity:S2083`, go to <https://rules.sonarsource.com/typescript/RSPEC-2083/>

tssecurity:S2083

tssecurity:S2631

tssecurity:S3649

tssecurity:S5131

tssecurity:S5146

tssecurity:S5696

tssecurity:S6096

</details>
