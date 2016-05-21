all: splash.png

splash.png: gimp/splash.xcf
	gimp -i --batch-interpreter=python-fu-eval -b - <../tools/convert.py
