all: building_block.png car1.png car2.png tree.png sunny.png

building_block.png car1.png car2.png tree.png sunny.png: gimp/building_block.xcf gimp/car1.xcf gimp/car2.xcf gimp/tree.xcf gimp/sunny.xcf
	gimp -i --batch-interpreter=python-fu-eval -b - <../tools/convert.py
