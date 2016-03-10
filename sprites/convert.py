import os
import gimpfu

def convert(filename):
    img = pdb.gimp_file_load(filename, filename)
    new_name = os.path.basename(filename.rsplit(".",1)[0] + ".png")
    layer = pdb.gimp_image_merge_visible_layers(img, gimpfu.CLIP_TO_IMAGE)

    pdb.gimp_file_save(img, layer, new_name, new_name)
    pdb.gimp_image_delete(img)

from glob import glob
for filename in glob("gimp/*.xcf"):
    convert(filename)

pdb.gimp_quit(1)
