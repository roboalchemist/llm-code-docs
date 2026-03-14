# Code Snippets and Recipes for Loguru

## Security considerations when using Loguru

Firstly, if you use `pickle` [https://docs.python.org/3/library/pickle.html#module-pickle] to load log messages (e.g. from the network), make sure the source is trustable or sign the data to verify its authenticity before deserializing it. If you do not take these precautions, malicious code could be executed by an attacker. You can read more details in this article: What’s so dangerous about pickles? [https://intoli.com/blog/dangerous-pickles/]

```
import hashlib
import hmac
import pickle

def client(connection):
    data = pickle.dumps("Log message")
    digest =  hmac.digest(b"secret-shared-key", data, hashlib.sha1)
    connection.send(digest + b" " + data)

def server(connection):
    expected_digest, data = connection.read().split(b" ", 1)
    data_digest = hmac.digest(b"secret-shared-key", data, hashlib.sha1)
    if not hmac.compare_digest(data_digest, expected_digest):
        print("Integrity error")
    else:
        message = pickle.loads(data)
        logger.info(message)

```