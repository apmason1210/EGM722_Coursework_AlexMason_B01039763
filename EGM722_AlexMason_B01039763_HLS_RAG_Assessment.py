#Import required modules
import os
import arcpy
from arcpy import env  
from arcpy.sa import *

def LULC_Reclassify():
    # Set the extent of the processing environment using a feature class, defined by the user and saved in 'InputDataAOI' folder as a shapefile 'HLS_AOI.shp'.
    arcpy.env.extent = r"C:\Users\Lieutenant\EGM722_Coursework_AlexMason_B01039763\InputDataAOI\HLS_AOI.shp"
    
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

def Mosaic_DEM():  #Mosaic the DEM tiles to a New Raster covering only the AOI polygon area.
    
    # Set the extent of the processing environment using a feature class, defined by the user and saved in 'InputDataAOI' folder as a shapefile 'HLS_AOI.shp'.
    arcpy.env.extent = r"C:\Users\Lieutenant\EGM722_Coursework_AlexMason_B01039763\InputDataAOI\HLS_AOI.shp"
        
    # Set processing environment, matching the folder location of the input DEM raster tiles 'InputDataDEM'.
    arcpy.env.workspace = r"C:\Users\Lieutenant\EGM722_Coursework_AlexMason_B01039763\InputDataDEM"

    # Get and print a list of TIFs from the workspace
    inputDEMs = arcpy.ListRasters("*", "TIF")
    for raster in inputDEMs:
            print(raster)

    # Set output raster folder location:
    outputDEM_Folder = r"C:\Users\Lieutenant\EGM722_Coursework_AlexMason_B01039763"

    # Set Ouput DEM file name:
    outputDEM_File = "HLS_AOI_2m_DEM.tif"

    # Set coordinate system to match the input DEMs:
    DEM_CoordinateSystem = r"C:\Users\Lieutenant\EGM722_Coursework_AlexMason_B01039763\BNG.prj" # the .prj file is provided in the github repository, specifically for British National Grid.

    # Set pixel type, matching the National LiDAR Programme input tiles, 32 bit float.
    pixel_type = "32_BIT_FLOAT"

    # Set the cell size of the output raster, to match the input DEM tiles, which for these dataset(s) is 2m pixels:
    cellsize = "2"

    # Set the number of bands for the output raster, just one, to record the elevation values:
    number_of_bands = "1"

    # Set the mosic method for the operation:
    mosaic_method = "LAST" # this is also the default option for the tool.
    
    # Set the Mosaic Colourmap Mode:
    mosaic_colormap_mode = "LAST" # This is the default for the tool.

    # Mosaic several TIFF images to a new TIFF image:
    arcpy.management.MosaicToNewRaster(inputDEMs, outputDEM_Folder, outputDEM_File, DEM_CoordinateSystem, pixel_type, cellsize, number_of_bands, mosaic_method, mosaic_colormap_mode)

Mosaic_DEM() # Run the Mosaic DEM function.

def Slope_2m(): # This function uses the Slope tool to first calculate Slope of the DTM in Degrees, 
                        # with horizontal pixel resolution matching the input DTM.
                            
    # Set processing environment, matching the folder location of the input 2m DTM raster 'HLS_AOI_2m_DEM.tif'.
    arcpy.env.workspace = r"C:\Users\Lieutenant\EGM722_Coursework_AlexMason_B01039763"

    # Pick up the name of the 2m DTM raster from the Mosaic function:
    inRaster = "HLS_AOI_2m_DEM.tif"  

    # specify the file namew of the ouput slope dataset:
    outRaster = "HLS_AOI_2m_Slope.tif" 
    
    # output the Slope as Degrees:
    outMeasurement = "DEGREE" 

    # Set the vertical scaling factor (z-factor) as 1. 
    # No scaling is required because the input DTM is horizontal units metres, and vertical units metres.
    zFactor = "1" 
    
    # Set the METHOD for the calculation based on planar (flat earth):
    method = "PLANAR"
    
    # Set the vertical Z value unit, as metres, to match the input DTM 2m raster:
    zUnit = "METER"

    # Execute Slope tool:
    arcpy.ddd.Slope(inRaster, outRaster, outMeasurement, zFactor, method, zUnit)
    
Slope_2m() # Run the Slope analysis function.

def SlopeAggregate_2to10(): # This function downsamples the Slope 2m resolution to a 10m resolution raster,
                        # while also also matching the geometry of the reclassified Land Use / Land Cover (LULC) 10m raster.
    
    # Set processing environment, matching the parent folder location for the analysis workflow:
    arcpy.env.workspace = r"C:\Users\Lieutenant\EGM722_Coursework_AlexMason_B01039763"
    
    # Set the extent environment to match the LULC reclassified raster:
    arcpy.env.extent = "\InputDataLULC\outReclassifyLULC.tif"

    # Define the input raster:
    in_raster = "HLS_AOI_2m_Slope.tif"
    
    # Define the Cell Factor to agreggate by. In this case, we are aggregating from 2m to 10m so a factor of 5:
    cell_factor = "5"
    
    # Define the aggregation statistical method:
    aggregation_type = "MEAN" # This setting defines that the MEAN values of the input slope cells are calculated and recorded to the output.
    
    # Define the Extent Handling method:
    extent_handling = "EXPAND" # This setting ensure the boundaries of the output raster are expanded from the input raster, 
                                # if required, to match the geometry.
    
    # Define how to handle cells with No Data:
    ignore_nodata = "DATA" # This setting ignores pixels with NoData when aggregating to the larger pixel.
    
    # Execute Aggregate
    outSlope10m = Aggregate(in_raster, cell_factor, aggregation_type, extent_handling, ignore_nodata)

    # Save the output to the environment workspace as a raster of data type TIF: 
    outSlope10m.save("HLS_AOI_10m_Slope.tif")
    
SlopeAggregate_2to10() # Run the rasample function.

def SlopeClassifyWildcat(): # This function reclassifies the 10m slope dataset from Degrees to 
                            # numerical values representing classes defined for the Wildcat 
                            # Slope Requirements in the instruction manual document. 
    
    #Set processing environment, matching the parent folder location for the project:
    env.workspace = r"C:\Users\Lieutenant\EGM722_Coursework_AlexMason_B01039763"
    
    # Set the extent of the processing environment using a feature class, defined by the user 
    # and saved in 'InputDataAOI' folder as a shapefile 'HLS_AOI.shp'.
    arcpy.env.extent = r"\InputDataAOI\HLS_AOI.shp"
    
    # Set local variables:
    # Set location of the input 10m Slope dataset:
    inRasterWildcatSlope = "HLS_AOI_10m_Slope.tif"

    # Set the field or band of the raster which holds the numerical slope values in degrees:
    reclassFieldSlope = "Value"

    # Set the reclassification table as a list of tuples, based on the reclassification table in the instruction document.
    # 0 to 3 degrees = 3; 3 to 7 degrees = 2; 7 to 90 degrees = 0
    remapWildcatSlope = RemapRange([[0,3,3],[3,7,2],[7,90,0]])
    
    # Execute Reclassify tool
    outReclassifySlopeWildcat = Reclassify(inRasterWildcatSlope, reclassFieldSlope, remapWildcatSlope, "NODATA")

    # Save the output as raster with format TIF.
    outReclassifySlopeWildcat.save("outReclassifySlopeWildcat.tif")
    
SlopeClassifyWildcat() # Run the reclassification for Wildcat Helicopter requirements.

def SlopeClassifyMerlin(): # This function reclassifies the 10m slope dataset from Degrees to 
                            # numerical values representing classes defined for the Merlin 
                            # Slope Requirements in the instruction manual document. 
    
    #Set processing environment, matching the parent folder location for the project:
    env.workspace = r"C:\Users\Lieutenant\EGM722_Coursework_AlexMason_B01039763"
    
    # Set the extent of the processing environment using a feature class, defined by the user 
    # and saved in 'InputDataAOI' folder as a shapefile 'HLS_AOI.shp'.
    arcpy.env.extent = r"\InputDataAOI\HLS_AOI.shp"
    
    # Set local variables:
    # Set location of the input 10m Slope dataset:
    inRasterMerlinSlope = "HLS_AOI_10m_Slope.tif"

    # Set the field or band of the raster which holds the numerical slope values in degrees:
    reclassFieldSlope = "Value"

    # Set the reclassification table as a list of tuples, based on the reclassification table in the instruction document.
    # 0 to 2 degrees = 3; 2 to 6 degrees = 2; 6 to 9 degrees = 1; 9 to 90 degrees = 0
    remapMerlinSlope = RemapRange([[0,2,3],[2,6,2],[6,9,1],[9,90,0]])
    
    # Execute Reclassify tool
    outReclassifySlopeMerlin = Reclassify(inRasterMerlinSlope, reclassFieldSlope, remapMerlinSlope, "NODATA")

    # Save the output as raster with format TIF.
    outReclassifySlopeMerlin.save("outReclassifySlopeMerlin.tif")
    
SlopeClassifyMerlin() # Run the reclassification for Wildcat Helicopter requirements.

def SlopeClassifyChinook(): # This function reclassifies the 10m slope dataset from Degrees to 
                            # numerical values representing classes defined for the Chinook 
                            # Slope Requirements in the instruction manual document. 
    
    #Set processing environment, matching the parent folder location for the project:
    env.workspace = r"C:\Users\Lieutenant\EGM722_Coursework_AlexMason_B01039763"
    
    # Set the extent of the processing environment using a feature class, defined by the user 
    # and saved in 'InputDataAOI' folder as a shapefile 'HLS_AOI.shp'.
    arcpy.env.extent = r"\InputDataAOI\HLS_AOI.shp"
    
    # Set local variables:
    # Set location of the input 10m Slope dataset:
    inRasterChinookSlope = "HLS_AOI_10m_Slope.tif"

    # Set the field or band of the raster which holds the numerical slope values in degrees:
    reclassFieldSlope = "Value"

    # Set the reclassification table as a list of tuples, based on the reclassification table in the instruction document.
    # 0 to 6 degrees = 3; 6 to 7 degrees = 2; 7 to 10 degrees = 1; 10 to 90 degrees = 0
    remapChinookSlope = RemapRange([[0,6,3],[6,7,2],[7,10,1],[10,90,0]])
    
    # Execute Reclassify tool
    outReclassifySlopeChinook = Reclassify(inRasterChinookSlope, reclassFieldSlope, remapChinookSlope, "NODATA")

    # Save the output as raster with format TIF.
    outReclassifySlopeChinook.save("outReclassifySlopeChinook.tif")
    
SlopeClassifyChinook() # Run the reclassification for Wildcat Helicopter requirements.


