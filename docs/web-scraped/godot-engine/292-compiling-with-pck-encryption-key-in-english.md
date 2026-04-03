# Compiling with PCK encryption key in English

# Compiling with PCK encryption key

The export dialog gives you the option to encrypt your PCK file with a 256-bit
AES key when releasing your project. This will make sure your scenes, scripts
and other resources are not stored in plain text and can not easily be ripped
by some script kiddie.
Of course, the key needs to be stored in the binary, but if it's compiled,
optimized and without symbols, it would take some effort to find it.
For this to work, you need to build the export templates from source,
with that same key.
Warning
This willnotwork if you use official, precompiled export templates.
It is absolutelyrequiredto compile your own export templates to use
PCK encryption.

## Step by step

- Generate a 256-bit AES key in hexadecimal format. You can use the aes-256-cbc variant fromthis service.Alternatively, you can generate it yourself usingOpenSSLcommand-line tools:opensslrand-hex32>godot.gdkeyThe output ingodot.gdkeyshould be similar to:# NOTE: Do not use the key below! Generate your own key instead.aeb1bc56aaf580cc31784e9c41551e9ed976ecba10d315db591e749f3f64890fYou can generate the key without redirecting the output to a file, but
that way you can minimize the risk of exposing the key.
Generate a 256-bit AES key in hexadecimal format. You can use the aes-256-cbc variant fromthis service.
Alternatively, you can generate it yourself usingOpenSSLcommand-line tools:

```
openssl rand -hex 32 > godot.gdkey
```

The output ingodot.gdkeyshould be similar to:

```
# NOTE: Do not use the key below! Generate your own key instead.
aeb1bc56aaf580cc31784e9c41551e9ed976ecba10d315db591e749f3f64890f
```

You can generate the key without redirecting the output to a file, but
that way you can minimize the risk of exposing the key.

- Set this key as environment variable in the console that you will use to
compile Godot, like this:Linux/macOSWindows (cmd)Windows (PowerShell)exportSCRIPT_AES256_ENCRYPTION_KEY="your_generated_key"setSCRIPT_AES256_ENCRYPTION_KEY=your_generated_key$env:SCRIPT_AES256_ENCRYPTION_KEY="your_generated_key"Note that the commands suggested above donotpersist the variables
across terminal sessions.
Set this key as environment variable in the console that you will use to
compile Godot, like this:

```
export SCRIPT_AES256_ENCRYPTION_KEY="your_generated_key"
```

```
set SCRIPT_AES256_ENCRYPTION_KEY=your_generated_key
```

```
$env:SCRIPT_AES256_ENCRYPTION_KEY="your_generated_key"
```

Note that the commands suggested above donotpersist the variables
across terminal sessions.

- Compile Godot export templates and set them as custom export templates
in the export preset options. If the environment variable is set correctly,
the following message is printed at the beginning of compilation:***IMPORTANT:CompilingGodotwithcustom`SCRIPT_AES256_ENCRYPTION_KEY`setasenvironmentvariable.
***Makesuretousetemplatescompiledwiththiskeywhenexportingaprojectwithencryption.
Compile Godot export templates and set them as custom export templates
in the export preset options. If the environment variable is set correctly,
the following message is printed at the beginning of compilation:

```
*** IMPORTANT: Compiling Godot with custom `SCRIPT_AES256_ENCRYPTION_KEY` set as environment variable.
*** Make sure to use templates compiled with this key when exporting a project with encryption.
```

- Set the encryption key in theEncryptiontab of the export preset:
Set the encryption key in theEncryptiontab of the export preset:
- Add filters for the files/folders to encrypt.By default, include filters
are empty andnothing will be encrypted.
Add filters for the files/folders to encrypt.By default, include filters
are empty andnothing will be encrypted.
- Export the project. The project should run with the files encrypted now.
Export the project. The project should run with the files encrypted now.

## Troubleshooting

If you get an error like below, it means the key wasn't properly included in
your Godot build. Godot is encrypting PCK file during export, but can't read
it at runtime.

```
ERROR: open_and_parse: Condition "String::md5(md5.digest) != String::md5(md5d)" is true. Returning: ERR_FILE_CORRUPT
   At: core/io/file_access_encrypted.cpp:103
```

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
