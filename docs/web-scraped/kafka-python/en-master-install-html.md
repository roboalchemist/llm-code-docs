# Source: https://kafka-python.readthedocs.io/en/master/install.html

Title: Install — kafka-python 2.3.0 documentation

URL Source: https://kafka-python.readthedocs.io/en/master/install.html

Published Time: Sat, 06 Dec 2025 15:30:04 GMT

Markdown Content:
[kafka-python](https://kafka-python.readthedocs.io/en/master/index.html)
Install with your favorite package manager

Latest Release[](https://kafka-python.readthedocs.io/en/master/install.html#latest-release "Link to this heading")
-------------------------------------------------------------------------------------------------------------------

Pip:

pip install kafka-python

Releases are also listed at [https://github.com/dpkp/kafka-python/releases](https://github.com/dpkp/kafka-python/releases)

Bleeding-Edge[](https://kafka-python.readthedocs.io/en/master/install.html#bleeding-edge "Link to this heading")
-----------------------------------------------------------------------------------------------------------------

git clone https://github.com/dpkp/kafka-python
pip install ./kafka-python

Optional crc32c install[](https://kafka-python.readthedocs.io/en/master/install.html#optional-crc32c-install "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------

Highly recommended if you are using Kafka 11+ brokers. For those kafka-python uses a new message protocol version, that requires calculation of crc32c, which differs from the zlib.crc32 hash implementation. By default kafka-python calculates it in pure python, which is quite slow. To speed it up we optionally support [https://pypi.python.org/pypi/crc32c](https://pypi.python.org/pypi/crc32c) package if it’s installed.

pip install 'kafka-python[crc32c]'

Optional ZSTD install[](https://kafka-python.readthedocs.io/en/master/install.html#optional-zstd-install "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------

To enable ZSTD compression/decompression, install python-zstandard:

>>> pip install 'kafka-python[zstd]'

Optional LZ4 install[](https://kafka-python.readthedocs.io/en/master/install.html#optional-lz4-install "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------

To enable LZ4 compression/decompression, install python-lz4:

>>> pip install 'kafka-python[lz4]'

Optional Snappy install[](https://kafka-python.readthedocs.io/en/master/install.html#optional-snappy-install "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------

### Install Development Libraries[](https://kafka-python.readthedocs.io/en/master/install.html#install-development-libraries "Link to this heading")

Download and build Snappy from [https://google.github.io/snappy/](https://google.github.io/snappy/)

Ubuntu:

apt-get install libsnappy-dev

OSX:

brew install snappy

From Source:

wget https://github.com/google/snappy/releases/download/1.1.3/snappy-1.1.3.tar.gz
tar xzvf snappy-1.1.3.tar.gz
cd snappy-1.1.3
./configure
make
sudo make install

### Install Python Module[](https://kafka-python.readthedocs.io/en/master/install.html#install-python-module "Link to this heading")

Install the python-snappy module

pip install 'kafka-python[snappy]'
