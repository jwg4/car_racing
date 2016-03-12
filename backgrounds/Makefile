all: bridge_.png road.png sky.png grass.png

road.png sky.png bridge.png grass.png: gimp/road.xcf gimp/sky.xcf gimp/bridge.xcf gimp/grass.xcf
	gimp -i --batch-interpreter=python-fu-eval -b - <convert.py

bridge_.png: bridge.png
	convert bridge.png -crop 78x60+90x0 bridge_.png

