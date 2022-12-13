# Proxier

Simple cli for download proxy list

## Installation

For linux
```commandline
python3 setup.py install
```

For windows

```commandline
py .\setup.py install
```

Usage

```commandline
proxier -h
```

Output:
```commandline
usage: proxier [-h] {http,socks4,socks5} ...

positional arguments:
  {http,socks4,socks5}
    http                Download http proxy
    socks4              Download socks4 proxy
    socks5              Download socks5 proxy

options:
  -h, --help            show this help message and exit
```