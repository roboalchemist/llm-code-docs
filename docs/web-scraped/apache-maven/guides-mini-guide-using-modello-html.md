# Source: https://maven.apache.org/guides/mini/guide-using-modello.html

Title: Guide to using Modello – Maven

URL Source: https://maven.apache.org/guides/mini/guide-using-modello.html

Markdown Content:
[](https://maven.apache.org/guides/mini/guide-using-modello.html)
[Modello](https://codehaus-plexus.github.io/modello/) is a tool for generating resources from a simple model. From a [simple model](https://codehaus-plexus.github.io/modello/modello.html) you can generate things like:

*   Java sources
*   XML serialization code for the model
*   XML deserialization code for model
*   Model documentation
*   XSD

A typical modello model looks like the following:

1.   `<model xmlns="http://codehaus-plexus.github.io/MODELLO/2.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"`
2.   `xsi:schemaLocation="http://codehaus-plexus.github.io/MODELLO/2.0.0 https://codehaus-plexus.github.io/modello/xsd/modello-2.0.0.xsd"`
3.   `xml.namespace="http://maven.apache.org/plugins/maven-archetype-plugin/archetype-descriptor/${version}"`
4.   `xml.schemaLocation="https://maven.apache.org/xsd/archetype-descriptor-${version}.xsd">`
5.   `<id>archetype-descriptor</id>`
6.   `<name>ArchetypeDescriptor</name>`
7.   `<description>`
8.   `<![CDATA[`
9.   `<p>This is a reference for the Archetype descriptor used to describe archetypes's metadata.</p>`
10.   `<p>The metadata about an archetype is stored in the <code>archetype-metadata.xml</code> file located`
11.   `in the <code>META-INF/maven</code> directory of its jar file.</p>]]>`
12.   `</description>`

14.   `<defaults>`
15.   `<default>`
16.   `<key>package</key>`
17.   `<value>org.apache.maven.archetype.metadata</value>`
18.   `</default>`
19.   `</defaults>`

21.   `<classes>`
22.   `<class rootElement="true" xml.tagName="archetype-descriptor">`
23.   `<name>ArchetypeDescriptor</name>`
24.   `<version>1.0.0+</version>`
25.   `<superClass>AbstractArchetypeDescriptor</superClass>`
26.   `<fields>`
27.   `<field xml.attribute="true">`
28.   `<name>name</name>`
29.   `<version>1.0.0+</version>`
30.   `<type>String</type>`
31.   `<required>true</required>`
32.   `<description>Name of the Archetype, that will be displayed to the user when choosing an archetype.</description>`
33.   `</field>`
34.   `<field xml.attribute="true">`
35.   `<name>partial</name>`
36.   `<version>1.0.0+</version>`
37.   `<type>boolean</type>`
38.   `<required>false</required>`
39.   `<description>Is this archetype representing a full Maven project or only parts?</description>`
40.   `</field>`
41.   `<field>`
42.   `<name>requiredProperties</name>`
43.   `<version>1.0.0+</version>`
44.   `<description>List of required properties to generate a project from this archetype.</description>`
45.   `<association>`
46.   `<type>RequiredProperty</type>`
47.   `<multiplicity>*</multiplicity>`
48.   `</association>`
49.   `</field>`
50.   `</fields>`
51.   `</class>`

53.   `<class>`
54.   `<name>ModuleDescriptor</name>`
55.   `<version>1.0.0+</version>`
56.   `<superClass>AbstractArchetypeDescriptor</superClass>`
57.   `<fields>`
58.   `<field xml.attribute="true">`
59.   `<name>id</name>`
60.   `<version>1.0.0+</version>`
61.   `<type>String</type>`
62.   `<required>true</required>`
63.   `<description>The module's artifactId.</description>`
64.   `</field>`
65.   `<field xml.attribute="true">`
66.   `<name>dir</name>`
67.   `<version>1.0.0+</version>`
68.   `<type>String</type>`
69.   `<required>true</required>`
70.   `<description>The module's directory.</description>`
71.   `</field>`
72.   `<field xml.attribute="true">`
73.   `<name>name</name>`
74.   `<version>1.0.0+</version>`
75.   `<type>String</type>`
76.   `<required>true</required>`
77.   `<description>The module's name.</description>`
78.   `</field>`
79.   `</fields>`
80.   `</class>`

82.   `<class>`
83.   `<name>AbstractArchetypeDescriptor</name>`
84.   `<version>1.0.0+</version>`
85.   `<fields>`
86.   `<field xdoc.separator="blank">`
87.   `<name>fileSets</name>`
88.   `<version>1.0.0+</version>`
89.   `<association>`
90.   `<type>FileSet</type>`
91.   `<multiplicity>*</multiplicity>`
92.   `</association>`
93.   `<required>true</required>`
94.   `<description>File sets definition.</description>`
95.   `</field>`
96.   `<field xdoc.separator="blank">`
97.   `<name>modules</name>`
98.   `<version>1.0.0+</version>`
99.   `<association>`
100.   `<type>ModuleDescriptor</type>`
101.   `<multiplicity>*</multiplicity>`
102.   `</association>`
103.   `<required>false</required>`
104.   `<description>Modules definition.</description>`
105.   `</field>`
106.   `</fields>`
107.   `</class>`

109.   `<class>`
110.   `<name>FileSet</name>`
111.   `<version>1.0.0+</version>`
112.   `<description><![CDATA[`
113.   `A fileset defines the way the project's files located in the jar file are used by the Archetype Plugin to generate a project.`
114.   `If file or directory name contains <code>__<i>property</i>__</code> pattern, it is replaced with corresponding property value.`
115.   `]]></description>`
116.   `<fields>`
117.   `<field xml.attribute="true">`
118.   `<name>filtered</name>`
119.   `<version>1.0.0+</version>`
120.   `<type>boolean</type>`
121.   `<required>false</required>`
122.   `<description><![CDATA[`
123.   `Filesets can be filtered, which means the selected files will be used as`
124.   `<a href="https://velocity.apache.org/engine/1.5/user-guide.html">Velocity templates</a>.`
125.   `They can be non-filtered, which means the selected files will be copied without modification.`
126.   `]]></description>`
127.   `</field>`
128.   `<field xml.attribute="true">`
129.   `<name>packaged</name>`
130.   `<version>1.0.0+</version>`
131.   `<type>boolean</type>`
132.   `<required>false</required>`
133.   `<description>Filesets can be packaged, which means the selected files will be generated/copied in a directory`
134.   `structure that is prepended by the package property. They can be non-packaged, which means that the selected`
135.   `files will be generated/copied without that prepend.</description>`
136.   `</field>`
137.   `<field xml.attribute="true">`
138.   `<name>encoding</name>`
139.   `<version>1.0.0+</version>`
140.   `<type>String</type>`
141.   `<required>false</required>`
142.   `<description>Encoding to use when filtering content.</description>`
143.   `</field>`
144.   `<field xml.attribute="true">`
145.   `<name>includeCondition</name>`
146.   `<version>1.2.0+</version>`
147.   `<type>String</type>`
148.   `<required>false</required>`
149.   `<description>A string value that should resolve to a boolean value to conditionally include filesets.`
150.   `This condition should be either a boolean as String or a velocity template language statement that resolves`
151.   `to a boolean value. If the descriptor contains includeCondition="${shouldInclude}" and the archetype has`
152.   `a (required) property like shouldInclude=true the fileset is included.</description>`
153.   `</field>`
154.   `<field>`
155.   `<name>directory</name>`
156.   `<version>1.0.0+</version>`
157.   `<type>String</type>`
158.   `<required>false</required>`
159.   `<defaultValue/>`
160.   `<description>The directory where the files will be searched for, which is also the directory where the`
161.   `project's files will be generated.</description>`
162.   `</field>`
163.   `<field>`
164.   `<name>includes</name>`
165.   `<version>1.0.0+</version>`
166.   `<association>`
167.   `<type>String</type>`
168.   `<multiplicity>*</multiplicity>`
169.   `</association>`
170.   `<required>false</required>`
171.   `<description>Inclusion definition "à la" Ant.</description>`
172.   `</field>`
173.   `<field>`
174.   `<name>excludes</name>`
175.   `<version>1.0.0+</version>`
176.   `<association>`
177.   `<type>String</type>`
178.   `<multiplicity>*</multiplicity>`
179.   `</association>`
180.   `<required>false</required>`
181.   `<description>Exclusion definition "à la" Ant.</description>`
182.   `</field>`
183.   `</fields>`
184.   `<codeSegments>`
185.   `<codeSegment>`
186.   `<code><![CDATA[`
187.   `public String toString()`
188.   `{`
189.   `return`
190.   `getDirectory() + " ("`
191.   `+ ( isFiltered() ? "Filtered" : "Copied" )`
192.   `+ "-"`
193.   `+ ( isPackaged() ? "Packaged" : "Flat" )`
194.   `+ ") ["`
195.   `+ org.codehaus.plexus.util.StringUtils.join( getIncludes().iterator(), ", " )`
196.   `+ " -- "`
197.   `+ org.codehaus.plexus.util.StringUtils.join( getExcludes().iterator(), ", " )`
198.   `+ "]";`

200.   `}`
201.   `]]></code>`
202.   `</codeSegment>`
203.   `</codeSegments>`
204.   `</class>`

206.   `<class>`
207.   `<name>RequiredProperty</name>`
208.   `<version>1.0.0+</version>`
209.   `<description>Definition of a property required when generating a project from this archetype.</description>`
210.   `<fields>`
211.   `<field xml.attribute="true">`
212.   `<name>key</name>`
213.   `<version>1.0.0+</version>`
214.   `<type>String</type>`
215.   `<required>true</required>`
216.   `<description>Key value of the property.</description>`
217.   `</field>`
218.   `<field>`
219.   `<name>defaultValue</name>`
220.   `<type>String</type>`
221.   `<required>false</required>`
222.   `<description>Default value of the property.</description>`
223.   `</field>`
224.   `<field>`
225.   `<name>validationRegex</name>`
226.   `<version>1.1.0+</version>`
227.   `<type>String</type>`
228.   `<required>false</required>`
229.   `<description>A regular expression used to validate the property.</description>`
230.   `</field>`
231.   `</fields>`
232.   `</class>`
233.   `</classes>`
234.   `</model>`

To utilize Modello, you would configure the `modello-maven-plugin` something like the following where you want to generate the Java sources for the model, the xpp3 serialization code and the xpp3 deserialization code (see [modello-plugin-xpp3](https://codehaus-plexus.github.io/modello/modello-plugins/modello-plugin-xpp3/) for more details):

1.   `<project xmlns="http://maven.apache.org/POM/4.0.0">`
2.   `...`
3.   `<build>`
4.   `<plugins>`
5.   `<plugin>`
6.   `<groupId>org.codehaus.modello</groupId>`
7.   `<artifactId>modello-maven-plugin</artifactId>`
8.   `<version>1.8.3</version>`
9.   `<executions>`
10.   `<execution>`
11.   `<goals>`
12.   `<!-- Generate the xpp3 reader code -->`
13.   `<goal>xpp3-reader</goal>`
14.   `<!-- Generate the xpp3 writer code -->`
15.   `<goal>xpp3-writer</goal>`
16.   `<!-- Generate the Java sources for the model itself -->`
17.   `<goal>java</goal>`
18.   `</goals>`
19.   `</execution>`
20.   `</executions>`
21.   `<configuration>`
22.   `<models>`
23.   `<model>src/main/mdo/archetype-descriptor.mdo</model>`
24.   `</models>`
25.   `<version>1.0.0</version>`
26.   `<useJava5>true</useJava5>`
27.   `</configuration>`
28.   `</plugin>`
29.   `</plugins>`
30.   `</build>`
31.   `...`
32.   `</project>`
