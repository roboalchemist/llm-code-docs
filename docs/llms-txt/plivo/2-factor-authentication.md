# Source: https://plivo.com/docs/messaging/use-cases/2-factor-authentication/2-factor-authentication.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Two-Factor Authentication

> Set up SMS-based two-factor authentication with OTP using Plivo APIs

<Tabs>
  <Tab title="Node">
    ## Overview

    This guide shows how to set up SMS-based two-factor authentication (2FA) using Plivo's APIs and Node.js. Authentication with a one-time password (OTP) delivered to users via SMS is an effective way to secure your application.

    ***

    ### Set up the demo application

    First, clone the [2FA demo repository from GitHub](https://github.com/plivo/2fa-node-demo) and install the dependencies.

    ```sh  theme={null}
    git clone [https://github.com/plivo/2fa-node-demo.git](https://github.com/plivo/2fa-node-demo.git)
    cd 2fa-node-demo
    npm install
    ```

    Next, edit `config.js`. Replace the auth placeholders with your credentials from the [Plivo console](https://cx.plivo.com/home). Add your Plivo phone number and set the `phlo_id` to `null`.

    ***

    ### A review of the code

    Here’s a walk-through of the key functions in the demo application.

    #### Step 1: Generate the OTP

    This function generates a random six-digit one-time password.

    ```js  theme={null}
    const code = Math.floor(100000 + Math.random() * 900000);
    ```

    #### Step 2: Send an SMS with the OTP

    This function sends an SMS message containing the OTP to the user’s number using Plivo’s [Send Message API](/message/api/send-message/).

    ```js  theme={null}
    sendVerificationCode_sms(DstNumber, Message) {
        const code = Math.floor(100000 + Math.random() * 900000);
        this.client.messages.create({
            src: this.app_number,
            dst: DstNumber,
            text: Message.replace('__code__', code),
        });
        return code;
    }
    ```

    #### Failover: Make a voice call with the OTP

    If the user doesn't receive the SMS, they can request the OTP via a voice call using Plivo's [Make a Call API](/voice/api/call/make-a-call/).

    ```js  theme={null}
    sendVerificationCode_call(DstNumber) {
        const code = Math.floor(100000 + Math.random() * 900000);
        this.client.calls.create(
            this.app_number, // from
            DstNumber, // to
            '[https://twofa-answerurl.herokuapp.com/answer_url/](https://twofa-answerurl.herokuapp.com/answer_url/)' + code // answer_url
        );
        return code;
    }
    ```

    #### Step 3: Verify the OTP

    This function checks if the OTP entered by the user matches the one stored in Redis.

    ```js  theme={null}
    router.get('/checkcode/:number/:code', function(req, res) {
        const number = (req.params.number);
        const code = (req.params.code);
        redisClient.get(`number:${number}:code`, function(err, originalCode) {
            if (originalCode == code) {
                redisClient.del(`number:${number}:code`);
                res.send(JSON.stringify({
                    'status': 'success',
                    'message': 'Codes match, number verified'
                }));
            } else {
                res.send(JSON.stringify({
                    'status': 'failure',
                    'message': 'Codes do not match'
                }));
            }
        });
    });
    ```

    ***

    ### Test

    First, start the Redis server.

    ```sh  theme={null}
    redis-server
    ```

    Then, run the application.

    ```sh  theme={null}
    node app.js
    ```

    Use a tool like [ngrok](https://ngrok.com/) to expose your local server to the internet, then open the ngrok URL in your browser to see the demo app.
  </Tab>

  <Tab title="Ruby">
    ## Overview

    This guide shows how to set up SMS-based two-factor authentication (2FA) using Plivo's APIs and Ruby. Authentication with a one-time password (OTP) delivered to users via SMS is an effective way to secure your application.

    ***

    ### Set up the demo application

    First, clone the [2FA demo repository from GitHub](https://github.com/plivo/2fa-ruby-demo) and install the dependencies.

    ```sh  theme={null}
    git clone [https://github.com/plivo/2fa-ruby-demo.git](https://github.com/plivo/2fa-ruby-demo.git)
    cd 2fa-ruby-demo
    bundle install
    ```

    Next, edit `config.yaml`. Replace the auth placeholders with your credentials from the [Plivo console](https://cx.plivo.com/home). Add your Plivo phone number and set the `phlo_id` to `null`.

    ***

    ### A review of the code

    Here’s a walk-through of the key functions in the demo application.

    #### Step 1: Generate the OTP

    This function generates a random six-digit one-time password.

    ```rb  theme={null}
    code = rand(100000..999999)
    ```

    #### Step 2: Send an SMS with the OTP

    This function sends an SMS message containing the OTP to the user’s number using Plivo’s [Send Message API](/message/api/send-message/).

    ```rb  theme={null}
    def send_verification_code_sms(dst_number, message)
      code = rand(100000..999999)
      @client.messages.create(
        src: @app_number,
        dst: [dst_number],
        text: message.gsub('__code__', code.to_s)
      )
      code
    rescue PlivoRESTError => e
      puts 'Exception: ' + e.message
    end
    ```

    #### Failover: Make a voice call with the OTP

    If the user doesn't receive the SMS, they can request the OTP via a voice call using Plivo's [Make a Call API](/voice/api/call/make-a-call/).

    ```rb  theme={null}
    def send_verification_code_call(dst_number)
      code = rand(100000..999999)
      @client.calls.create(
        @app_number,
        [dst_number],
        "[https://twofa-answerurl.herokuapp.com/answer_url/#](https://twofa-answerurl.herokuapp.com/answer_url/#){code}"
      )
      code
    rescue PlivoRESTError => e
      puts 'Exception: ' + e.message
    end
    ```

    #### Step 3: Verify the OTP

    This function checks if the OTP entered by the user matches the one stored in Redis.

    ```rb  theme={null}
    get '/checkcode/:number/:code' do
      number = params['number']
      code = params['code']
      original_code = r.get("number:#{number}:code")

      content_type :json
      if original_code == code
        r.del("number:#{number}:code")
        return { status: 'success', message: 'Codes match, number verified' }.to_json
      else
        return { status: 'failure', message: 'Codes do not match' }.to_json
      end
    end
    ```

    ***

    ### Test

    First, start the Redis server.

    ```sh  theme={null}
    redis-server
    ```

    Then, run the application.

    ```shell  theme={null}
    ruby app.rb
    ```

    Use a tool like [ngrok](https://ngrok.com/) to expose your local server to the internet, then open the ngrok URL in your browser to see the demo app.
  </Tab>

  <Tab title="Python">
    ## Overview

    This guide shows how to set up SMS-based two-factor authentication (2FA) using Plivo's APIs and Python. Authentication with a one-time password (OTP) delivered to users via SMS is an effective way to secure your application.

    ***

    ### Set up the demo application

    First, clone the [2FA demo repository from GitHub](https://github.com/plivo/2fa-python-demo) and install the dependencies.

    ```sh  theme={null}
    git clone [https://github.com/plivo/2fa-python-demo.git](https://github.com/plivo/2fa-python-demo.git)
    cd 2fa-python-demo
    pip install -r requirements.txt
    ```

    Next, edit `settings.py`. Replace the auth placeholders with your credentials from the [Plivo console](https://cx.plivo.com/home). Add your Plivo phone number and set the `phlo_id` to `None`.

    ***

    ### A review of the code

    Here’s a walk-through of the key functions in the demo application.

    #### Step 1: Generate the OTP

    This function generates a random six-digit one-time password.

    ```py  theme={null}
    import random
    code = random.randint(100000, 999999)
    ```

    #### Step 2: Send an SMS with the OTP

    This function sends an SMS message containing the OTP to the user’s number using Plivo’s [Send Message API](/message/api/send-message/).

    ```py  theme={null}
    def send_verification_code_sms(self, dst_number, message_text):
        code = random.randint(100000, 999999)
        try:
            response = self.client.messages.create(
                src=self.app_number,
                dst=dst_number,
                text=message_text.replace('__code__', str(code))
            )
            return code, response
        except PlivoRestError as e:
            print(e)
    ```

    #### Failover: Make a voice call with the OTP

    If the user doesn't receive the SMS, they can request the OTP via a voice call using Plivo's [Make a Call API](/voice/api/call/make-a-call/).

    ```py  theme={null}
    def send_verification_code_voice(self, dst_number, code):
        try:
            response = self.client.calls.create(
                from_=self.app_number,
                to_=dst_number,
                answer_url=f"[https://twofa-answerurl.herokuapp.com/answer_url/](https://twofa-answerurl.herokuapp.com/answer_url/){code}",
                answer_method="GET",
            )
            return response
        except PlivoRestError as e:
            print(e)
    ```

    #### Step 3: Verify the OTP

    This function checks if the OTP entered by the user matches the one stored in Redis.

    ```py  theme={null}
    @app.route("/checkcode/<number>/<code>")
    def check_code(number, code):
        original_code = current_app.redis.get(f"number:{number}:code")
        if original_code == code:
            current_app.redis.delete(f"number:{number}:code")
            return jsonify({"status": "success", "message": "Codes match, number verified"}), 200
        else:
            return jsonify({"status": "failure", "message": "Codes do not match"}), 404
    ```

    ***

    ### Test

    First, start the Redis server.

    ```sh  theme={null}
    redis-server
    ```

    Then, run the application.

    ```shell  theme={null}
    flask run
    ```

    Use a tool like [ngrok](https://ngrok.com/) to expose your local server to the internet, then open the ngrok URL in your browser to see the demo app.
  </Tab>

  <Tab title="PHP">
    ## Overview

    This guide shows how to set up SMS-based two-factor authentication (2FA) using Plivo's APIs and PHP. Authentication with a one-time password (OTP) delivered to users via SMS is an effective way to secure your application.

    ***

    ### Set up the demo application

    First, clone the [2FA demo repository from GitHub](https://github.com/plivo/2fa-php-demo) and install the dependencies.

    ```sh  theme={null}
    git clone [https://github.com/plivo/2fa-php-demo.git](https://github.com/plivo/2fa-php-demo.git)
    cd 2fa-php-demo
    composer install
    ```

    Next, edit `config.ini`. Replace the auth placeholders with your credentials from the [Plivo console](https://cx.plivo.com/home). Add your Plivo phone number and set the `phlo_id` to `null`.

    ***

    ### A review of the code

    Here’s a walk-through of the key functions in the demo application.

    #### Step 1: Generate the OTP

    This function generates a random six-digit one-time password.

    ```php  theme={null}
    $code = random_int(100000, 999999);
    ```

    #### Step 2: Send an SMS with the OTP

    This function sends an SMS message containing the OTP to the user’s number using Plivo’s [Send Message API](/message/api/send-message/).

    ```php  theme={null}
    function send_verification_code_sms($dst_number, $message) {
        $code = random_int(100000, 999999);
        try {
            $this->client->messages->create([
                "src" => $this->config['app_number'],
                "dst" => [$dst_number],
                "text" => str_replace("__code__", $code, $message)
            ]);
            return $code;
        } catch (PlivoRestException $ex) {
            print_r($ex);
        }
    }
    ```

    #### Failover: Make a voice call with the OTP

    If the user doesn't receive the SMS, they can request the OTP via a voice call using Plivo's [Make a Call API](/voice/api/call/make-a-call/).

    ```php  theme={null}
    function send_verification_code_call($dst_number) {
        $code = random_int(100000, 999999);
        try {
            $this->client->calls->create(
                $this->config['app_number'],
                [$dst_number],
                '[https://twofa-answerurl.herokuapp.com/answer_url/'.$code](https://twofa-answerurl.herokuapp.com/answer_url/'.$code),
                'POST'
            );
            return $code;
        } catch (PlivoRestException $ex) {
            print_r($ex);
        }
    }
    ```

    #### Step 3: Verify the OTP

    This function checks if the OTP entered by the user matches the one stored in Redis.

    ```php  theme={null}
    $number = $param[2];
    $code   = $param[3];
    $original_code = $redis_client->get('number:' . $number . ':code');

    if ($original_code == $code) {
        $redis_client->del('number:' . $number . ':code');
        // Logic for success
    } else {
        // Logic for failure
    }
    ```

    ***

    ### Test

    First, start the Redis server.

    ```sh  theme={null}
    redis-server
    ```

    Then, run the application.

    ```shell  theme={null}
    php -S localhost:8000
    ```

    Use a tool like [ngrok](https://ngrok.com/) to expose your local server to the internet, then open the ngrok URL in your browser to see the demo app.
  </Tab>

  <Tab title=".NET">
    ## Overview

    This guide shows how to set up SMS-based two-factor authentication (2FA) using Plivo's APIs and .NET. Authentication with a one-time password (OTP) delivered to users via SMS is an effective way to secure your application.

    ***

    ### Set up the demo application

    First, clone the [2FA demo repository from GitHub](https://github.com/plivo/2fa-dotnet-demo) and open the project in Visual Studio.

    ```sh  theme={null}
    git clone [https://github.com/plivo/2fa-dotnet-demo.git](https://github.com/plivo/2fa-dotnet-demo.git)
    cd 2fa-dotnet-demo
    ```

    Next, edit `appsettings.json`. Replace the auth placeholders with your credentials from the [Plivo console](https://cx.plivo.com/home). Add your Plivo phone number and set the `PhloId` to `null`.

    ***

    ### A review of the code

    Here’s a walk-through of the key functions in the demo application.

    #### Step 1: Generate the OTP

    This function generates a random six-digit one-time password.

    ```cs  theme={null}
    Random r = new Random();
    var code = r.Next(100000, 999999);
    ```

    #### Step 2: Send an SMS with the OTP

    This function sends an SMS message containing the OTP to the user’s number using Plivo’s [Send Message API](/message/api/send-message/).

    ```cs  theme={null}
    public int SendVerificationCodeSms(String DstNumber, String Message)
    {
        Random r = new Random();
        var code = r.Next(100000, 999999);
        var response = Client.Message.Create(
            src: AppNumber,
            dst: new List<String> { DstNumber },
            text: Message.Replace("__code__", code.ToString())
        );
        return code;
    }
    ```

    #### Failover: Make a voice call with the OTP

    If the user doesn't receive the SMS, they can request the OTP via a voice call using Plivo's [Make a Call API](/voice/api/call/make-a-call/).

    ```cs  theme={null}
    public int SendVerificationCodeCall(String DstNumber)
    {
        Random r = new Random();
        var code = r.Next(100000, 999999);
        var response = Client.Call.Create(
            to: new List<String> { DstNumber },
            from: AppNumber,
            answerMethod: "POST",
            answerUrl: "[https://twofa-answerurl.herokuapp.com/answer_url/](https://twofa-answerurl.herokuapp.com/answer_url/)" + code
        );
        return code;
    }
    ```

    #### Step 3: Verify the OTP

    This function checks if the OTP entered by the user matches the one stored in Redis.

    ```cs  theme={null}
    public string Index(string number, string code)
    {
        ConnectionMultiplexer redis = ConnectionMultiplexer.Connect(_configuration.GetValue<string>("RedisHost"));
        IDatabase conn = redis.GetDatabase();
        string key = $"number:{number}:code";
        var compare_code = (string)conn.StringGet(key);

        Verification verification = new Verification();
        if (compare_code == code)
        {
            conn.KeyDelete(key);
            verification.status = "success";
            verification.message = "Number verified";
        }
        else
        {
            verification.status = "failure";
            verification.message = "Codes do not match";
        }
        return JsonConvert.SerializeObject(verification);
    }
    ```

    ***

    ### Test

    First, start the Redis server.

    ```sh  theme={null}
    redis-server
    ```

    Then, build and run the application from Visual Studio. Use a tool like [ngrok](https://ngrok.com/) to expose your local server to the internet, then open the ngrok URL in your browser to see the demo app.
  </Tab>
</Tabs>
