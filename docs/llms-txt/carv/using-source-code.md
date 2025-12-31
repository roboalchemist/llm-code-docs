# Source: https://docs.carv.io/carv-ecosystem/verifier-nodes/join-mainnet-verifier-nodes/operating-a-verifier-node/running-in-cli/using-source-code.md

# Using Source Code

{% hint style="info" %}
Note that the configuration may change while testing. Please check this page consistently for operation info.
{% endhint %}

#### Before you start

The verifier is written in Golang. Before you start, you should make sure you have Golang installed correctly. For more details check: <https://go.dev/doc/install>.

#### Clone the source code

The verifier code is open source and currently in development. You can clone the GitHub repository and build the source: <https://github.com/carv-protocol/verifier>.

<pre class="language-bash"><code class="lang-bash"><strong>git clone https://github.com/carv-protocol/verifier.git &#x26;&#x26; \
</strong><strong>cd verifier &#x26;&#x26; \
</strong><strong>make build
</strong></code></pre>

**Run via binary program**

After executing `make build` or `make all`, the verifier executable file will be compiled into the `./bin` directory. You need to switch to the `./bin` directory before executing verifier. run

```
cd bin
```

If this is your first time running verifier, you need to specify a private key. The private key will sign the verification transaction.

{% hint style="info" %}
**Never expose your main account's private key. Always generate a brand new private key for operating the node, otherwise generate a new one using the \`**&#x67;enerate-keystor&#x65;**\` command below.**
{% endhint %}

The private key can be passed to the verifier through startup parameters, or written into the configuration file.

**Through startup parameters**

If you already have a brand new private key generated, you can start your node with the command below.

{% hint style="info" %}
The private key can be any brand new private key. If the key doesn't hold the CARV node license, you need to go to <https://explorer.carv.io/verifiers> to delegate your license to this new key.
{% endhint %}

{% hint style="info" %}
Commission rate can be set between 0-10. 0 means you don't take any commission from delegators. 10 means you take 10% of the rewards from delegators.
{% endhint %}

```
# Pass the pre-generated private key in clear text
./verifier -private-key <Your Private Key> -reward-address <Your Reward Address> -commission-rate <Your Commission Rate>

# By specifying keystore
./verifier -keystore-path <Path to keystore file> -keystore-password <keystore password> -reward-address <Your Reward Address> -commission-rate <Your Commission Rate>
```

In order to facilitate user operation, verifier provides a tool to generate a new keystore, run

```
./verifier -generate-keystore -keystore-path <path to generate your keystore file>
```

After running the command, you will be prompted to enter a password for the keystore. After entering the password, the keystore file will be generated in the specified path. And then you can run the verifier with the keystore file path and password before you delegate to the keystore address.

{% hint style="info" %}
Same for Keystore. Before you run the verifier, you must delegate to the keystore address. After the delegation is successful, you can run the verifier again. Delegated address you can get from the terminal after generating the keystore. You can delegate your License through the explorer <https://explorer.carv.io/verifiers>.
{% endhint %}

**Through configuration file**

If you prefer to config your own parameters, including RPC url, private key mode, etc. you can operate your node using config file, check details below:

1. Set `wallet.mode` in the configuration file (`../configs/config.yaml`)  to `1`,
2. Write the plain text private key into `wallet.private_key`,
3. Write your reward address into `wallet.reward_claimer_addr`,
4. Write your commission rate into `wallet.commission_rate`. Then run

```
./verifier -conf ../configs/config.yaml 
```

Configure the path and password of the keystore:

1. Set `wallet.mode` in the configuration file (`../configs/config.yaml`) to `2`,
2. Write the path and password of the keystore file into `wallet.keystore_path`
3. Write the keystore password into `wallet.keystore_password`.
4. Write your reward address into `wallet.reward_claimer_addr`,
5. Write your commission rate into `wallet.commission_rate`. Then run

```
./verifier -conf ../configs/config.yaml
```
