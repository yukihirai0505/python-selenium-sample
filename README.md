# Get Started

python 3.5.3

install requirements

`pip install -r example/requirements.txt`

execute this example python file

`python example/scraping.py`

## scraping.py

Root directory scraping.py uses `webkit2png`.
So it needs to webkit2png command.

`brew install webkit2png`

## About webkit2png

In my case, webkit2png command doesn't work.
I got this error.

```
Python[16938:2657011] App Transport Security has blocked a cleartext HTTP (http://) resource load since it is insecure. Temporary exceptions can be configured via your app's Info.plist file.
 ... something went wrong: The resource could not be loaded because the App Transport Security policy requires the use of a secure connection.
```

So I tried this one.

[https://github.com/bendalton/webkit2png/commit/9a96ac8977c386a84edb674ca1518e90452cee88](https://github.com/bendalton/webkit2png/commit/9a96ac8977c386a84edb674ca1518e90452cee88)
from: [http://stackoverflow.com/questions/32916052/python-app-transport-security-error-under-el-capitan](http://stackoverflow.com/questions/32916052/python-app-transport-security-error-under-el-capitan)

`/usr/local/Cellar/webkit2png/0.7/bin/webkit2png`

Around line 420

```
+    # Handles ATS HTTPS requirement introduced in El Cap
+    if options.ignore_ssl_check:
+        AppKit.NSBundle.mainBundle().infoDictionary()['NSAppTransportSecurity'] = dict(NSAllowsArbitraryLoads = True)
```

Then it works

`webkit2png --ignore-ssl-check [options] [http://example/]`