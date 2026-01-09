## What is this?
Playstation Vue Proof of concept using JavaScript injection via mitm proxy.

Targets version 1.01. This is a [userland exploit](https://consolemods.org/wiki/PS4:FAQ#Userland_Exploits).

## Dependencies
python 3, mitmproxy

## How to set up
Install the Playstation Vue base application from [here](http://gs2.ww.prod.dl.playstation.net/gs2/appkgo/prod/CUSA00960_00/2/f_5b45e504cfc157f23167959e82c3d9816ed717f563197d982dc7fb669434972a/f/UT0016-CUSA00960_00-COBRAPCKGE000000.pkg). This is the official playstation.net link.

Follow the bypass psncheck guide in [Vue-mitm-poc/download0/README.md](https://github.com/earthonion/Vue-mitm-poc/blob/main/download0/README.md).

Run `mitmproxy -s proxy.py`.

Connect to the proxy on your PS4.

Run Playstation Vue.

## License
GPL © earthonion