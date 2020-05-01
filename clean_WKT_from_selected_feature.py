import re
layer = iface.activeLayer()
object = layer.selectedFeatures()[0]
geom_text = object.geometry().asWkt()
patch_text = re.sub('\.[0-9]*','',geom_text)
print(patch_text)