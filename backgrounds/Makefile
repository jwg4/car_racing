all: bridge_.png road.png sky.png

road.png sky.png bridge.png: gimp/road.xcf gimp/sky.xcf gimp/bridge.xcf
	gimp -i --batch-interpreter=python-fu-eval -b - <convert.py

bridge_.png: bridge.png
	convert bridge.png -crop 78x60+90x0 bridge_.png

