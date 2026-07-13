#Import required modules
import os
import arcpy
from arcpy import env  
from arcpy.sa import *

#Set processing environment, matching the extent of the input LULC raster tile.
env.workspace = r"C:\Users\Lieutenant\EGM722_Coursework_AlexMason_B01039763\InputDataLULC"

# Set local variables:
#Set location of the input LULC dataset.
inRasterLULC = r"C:\Users\Lieutenant\EGM722_Coursework_AlexMason_B01039763\InputDataLULC\LCM.tif"

# Set the field or band of the raster which holds the numerical land classes.
reclassFieldLULC = "Value"

# Set the reclassification table as a list of tuples, based on the reclassification table in the instruction document.
remapLULC = RemapValue([[1,0],[2,0],[3,2],[4,3],[5,3],[6,3],[7,3],[8,0],[9,0],[10,1],[11,0],[12,1],[13,0],[14,0],[15,0],[16,2],[17,1],[18,1],[19,1],[20,0],[21,0]])

# Execute Reclassify tool
outReclassifyLULC = Reclassify(inRasterLULC, reclassFieldLULC, remapLULC, "NODATA")

# Save the output 
outReclassifyLULC.save("outReclassifyLULC.tif")



