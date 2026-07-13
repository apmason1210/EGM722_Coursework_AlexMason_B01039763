#Import required modules
import os
import arcpy
from arcpy import env  
from arcpy.sa import *

def LULC_Reclassify():
    #Set processing environment, matching the folder location of the input LULC raster tile.
    env.workspace = r"C:\Users\Lieutenant\EGM722_Coursework_AlexMason_B01039763\InputDataLULC"

    # Set local variables:
    # Set location of the input LULC dataset.
    inRasterLULC = r"C:\Users\Lieutenant\EGM722_Coursework_AlexMason_B01039763\InputDataLULC\LCM.tif"

    # Set the field or band of the raster which holds the numerical land classes.
    reclassFieldLULC = "Value"

    # Set the reclassification table as a list of tuples, based on the reclassification table in the instruction document.
    remapLULC = RemapValue([[1,0],[2,0],[3,2],[4,3],[5,3],[6,3],[7,3],[8,0],[9,0],[10,1],[11,0],[12,1],[13,0],[14,0],[15,0],[16,2],[17,1],[18,1],[19,1],[20,0],[21,0]])

    # Execute Reclassify tool
    outReclassifyLULC = Reclassify(inRasterLULC, reclassFieldLULC, remapLULC, "NODATA")

    # Save the output 
    outReclassifyLULC.save("outReclassifyLULC.tif")

LULC_Reclassify()

def Mosaic_DEM():  #Mosaic the DEM tiles to New Raster covering the AOI polygon area.
    # Set the extent of the processing environment using a feature class, defined by the user and saved in 'InputDataAOI' folder as a shapefile 'HLS_AOI.shp'.
    arcpy.env.extent = r"C:\Users\Lieutenant\EGM722_Coursework_AlexMason_B01039763\InputDataAOI\HLS_AOI.shp"
        
    # Set processing environment, matching the folder location of the input DEM raster tiles 'InputDataDEM'.
    arcpy.env.workspace = r"C:\Users\Lieutenant\EGM722_Coursework_AlexMason_B01039763\InputDataDEM"


    # Set input rasters variable:
    def inputDEMsList():
        contents = arcpy.env.workspace = r"C:\Users\Lieutenant\EGM722_Coursework_AlexMason_B01039763\InputDataDEM"
        arcpy.ListRasters("*", ".TIF")
    inputDEMsList() # Assign raster list to inputDEMs variable.
    print(inputDEMsList())

    # this method does not work: r"C:\Users\Lieutenant\EGM722_Coursework_AlexMason_B01039763\InputDataDEM"


    # Set output raster folder location:
    outputDEM_Folder = r"C:\Users\Lieutenant\EGM722_Coursework_AlexMason_B01039763"

    # Set Ouput DEM file name:
    outputDEM_File = "HLS_AOI_1m_DEM.tif"

    # Set coordinate system to match the input DEMs:
    DEM_CoordinateSystem = r"C:\Users\Lieutenant\EGM722_Coursework_AlexMason_B01039763\BNG.prj" # the .prj file is provided in the github repository, specifically for British National Grid.

    # Set pixel type, matching the National LiDAR Programme input tiles, 32 bit float.
    pixel_type = "32_BIT_FLOAT"

    # Set the cell size of the output raster, to match the input DEM tiles:
    cellsize = "1"

    # Set the number of bands for the output raster:
    number_of_bands = "1"

    # Set the mosic method for the operation:
    mosaic_method = "LAST" # this is also the default option for the tool.

    # Set the Mosaic Colourmap Mode:
    mosaic_colormap_mode = "LAST" # This is the default for the tool.

    # Mosaic several TIFF images to a new TIFF image:
    arcpy.management.MosaicToNewRaster(inputDEMs, outputDEM_Folder, outputDEM_File, DEM_CoordinateSystem, pixel_type, cellsize, number_of_bands, mosaic_method, mosaic_colormap_mode)


