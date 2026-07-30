Setup and Installation
Prerequisites
This project has been written and developed using ArcGIS Pro version 3.5. Users of the HLS RAG Assessment MUST have a LOCAL instance of ArcGIS Pro 3.XX installed on their machine, with active Basic, Standard or Advanced license(s). In addition, users must have active extensions of Spatial Analyst and 3D Analyst.
See Esri documentation on how to install ArcGIS Pro 3.5 here:
•	Download ArcGIS Pro—ArcGIS Pro | Documentation
•	Install ArcGIS Pro—ArcGIS Pro | Documentation

Python Environment
The ArcGIS Pro App is built on top of a Conda environment. The HLS script uses the default Conda environment which comes as part of the installation of ArcGIS Pro 3.XX, called Arcgispro-py3. This environment file is too large to host via GitHub; users must ensure they have the correct python environment installed and active from within ArcGIS Pro.
To do this, open an instance of ArcGIS Pro, then go to Settings > Package Manager. Next, on the right-hand side, click the dropdown for Active Environment, and select arcgispro-py3. Then click the back arrow at top left of the screen. See also Package Manager—ArcGIS Pro | Documentation and Using ArcGIS Pro 3.0 and later | ArcGIS API for Python | Esri Developer. The included list of dependencies is very long. Explore the contents within the package manager pane, if you wish.
Most of the HLS script uses tools from the ArcPy toolset, as well as some from Sys. It has been written / developed within ArcGIS Pro 3.5.  Users can find more information about ArcPy at the following link: ArcPy (What is ArcPy?—ArcGIS Pro | Documentation.
Link to the GitHub Repository
The github repository can be found here:
https://github.com/apmason1210/EGM722_Coursework_AlexMason_B01039763
Structure / Contents of the repository:
The repository should contain the following:
•	.idea
•	EGM722_Coursework_DevProject
•	InputDataAOI
o	HLS_AOI.shp (and associated files)
o	The shapefile polygon is set as test area over Salisbury Plain
•	InputDataDEM
o	This should contain test datasets over Salisbury Plain area
•	InputDataLULC
o	LCM.tif
o	This is Land Use / Land Cover for the Salisbury Plain AOI
•	LayerFiles
•	.gitignore
•	BNG.prj
•	EGM722_AlexMason_B01039763_HLS_RAG_Assessment.py (this is the primary script)
•	LICENSE
•	README.md
•	environment.yml

Using GitHub to access and clone the repository
Setting up a GitHub account
If you do not have one already, go to GitHub and click ‘Sign up’ in the top right-hand corner of the screen. Follow the in-browser instructions to create your account. Once you have done so, move on.

Installing Git
If you don’t have Git installed on your PC already, follow the following instructions.
Go to https://git-scm.com/downloads and choose the correct version for your operating system. ArcGIS Pro only runs on windows machines, so you will likely require a Windows OS version. Once identified, follow the wizard that is downloaded from your selection. 
Bob McNabb (© Copyright 2020-2026, Creative Commons License) has produced written instructions which you may choose to follow for more detailed settings within the wizard, found here: installing git — space cameras and glaciers

Installing GitHub Desktop
GitHub can be used within a browser, or from the GitHub Desktop app. To download the app, follow the link here: https://desktop.github.com/ 
Follow the installer instructions to download and install it on your local machine and ensure to install within your user space. Once installed, open it and log in to your GitHub account, and authorise GitHub Desktop to access your account.

Forking the repository
First, make sure you are logged in your GitHub account and go to the master repository for the HLS project, which can be found here: https://github.com/apmason1210/EGM722_Coursework_AlexMason_B01039763
In the top right-hand corner, click the Fork button. This will create a fork and copy the whole repository into your own account. After a while, you should see a window with [your username] / [repository name] at the top. You will have successfully forked the repository.  Make a note of the repository URL.

Cloning the repository
This instruction uses GitHub Desktop.
Once the repository is forked (previous step), you can clone the repository, which downloads it to a defined file location on your PC. Open Github Desktop. On the splash screen, you should see a list of your repositories. Click ‘Clone a repository from the internet’ and select the [your username] / EGM722_Coursework_AlexMason_B01039763 option. 
Specify a LOCAL file path to save the repository and record this location for future use. You will need it when sourcing and prepping the input data; as well as adding as folder connections in ArcGIS Pro or running the script from the Command Line, described later.  Finally, select the ‘For my own purposes’ option and hit continue.
You should now have a cloned version of the GitHub repository on your GitHub account and locally on your machine.

IMPORTANT: Setting the environment workspace within the script
Open the EGM722_AlexMason_B01039763_HLS_RAG_Assessment.py file from the repository, using Notebook or any Python IDE. Over-write the file path on line 8, which defines the variable home_folder. Input the file path to your cloned repository here. Save the python file and close Notebook or the IDE.

Sourcing Data
The script included has been written for use over areas of interest within Great Britain. As such, the coordinate system used throughout is OSGB36 / British National Grid - United Kingdom Ordnance Survey (EPSG: 27700). This is provided as a .prj file within the repository (BNG.prj).
The repository is supplied with an area of interest (AOI) shapefile defined over Salisbury Plain. To source your own datasets for an AOI, follow the below steps. 

Create the AOI shapefile:
•	Within ArcGIS Pro, you can either pull in the HLS_AOI.shp from the repository, OR create your own new shapefile, ensuring it is polygon type and has British National Grid coordinate system applied.
•	Start editing this layer, and define your new AOI
•	Ensure the shapefile has only one record (one rectangle) defined
•	Save the edits.
•	Make sure any output / final file is saved as ‘HLS_AOI.shp’ and is saved within  ‘InputDataAOI’ inside your repository location.

Digital Terrain Model (DTM) data
•	The example data held within the GitHub repository has been sourced from the National LiDAR Programme. Data can be accessed and downloaded from the following website: Defra Data Services Platform
•	Using the platform, draw a polygon AOI that roughly equates to your defined HLS_AOI.shp. Unfortunately, the platform does not accept upload of shapefiles.
•	Under Layers button in top right, select ‘LiDAR Composite DTM 2m 2022’. The menu should populate with the available tiles covering your AOI.
•	Then click Download. The platform will begin downloading your tiles as individual zip files for each one in turn. This may take a while! Be warned, the file sizes are quite large.
•	Once all have been downloaded, unzip each package in turn and save to a local area on your PC. You will need to extract all of the files individually. Each package contains a geotiff and associated files. 
•	Clear out the contents of ‘InputDataDEM’ inside the repository.
•	After unzipping, for every tile, select the .tfw, .tif, .tif.aux and .tif.xml files. Copy these files into your empty InputDataDEM folder, inside the local repository. Leave behind the geopackages (.gpkg), which are not needed. Repeat this for all tiles downloaded.

Land Use / Land Cover (LULC) data
•	The example supplied within the GitHub repository has been sourced from UK Centre for Ecology & Hydrology (UKCEH) Land Cover Maps, available at: UKCEH Land Cover Maps | UK Centre for Ecology & Hydrology
•	The Land Cover Map programme aims to produced repeat analysis each year. The example data used is from the Land Cover Map 2024 (LCM2024), specifically the Land Cover Map 2024 (10m classified pixels, GB) data package. 
•	Users can access these data via the following link: Land Cover Map 2024 (10m classified pixels, GB) - EIDC
•	New users will need to create a free account to access the download platform.
•	At the above link, go to ‘Download’ then ‘Order the Data’; login using your credentials
•	After logging in, you will be presented with another web map. Select the option to ‘Draw a boundary on the map’. Select the ‘Draw a rectangle’ tool, the small grey square on left edge of map frame. 
•	Click to draw your AOI, approximately equal to your HLS_AOI shapefile.
•	Hit the ‘Submit’ button at the bottom of the screen. The platform will give you an order details window, with State = PROCESSING. You will receive emails confirming your order and once it is ready for download.
•	Data once downloaded, must be unzipped and the contained .tif file should be copied into the ‘InputDataLULC’ folder, ensuring the file name is ‘LCM.tif’
How to run the script using ArcGIS Pro 
(see also Python window—ArcGIS Pro | Documentation):
1.	Start an instance of ArcGIS Pro
2.	Choose ‘Start without a template’ OR start a new map, and save it to your user area on disk.
3.	In the catalogue panel on the right, add a folder connection to your cloned repository.
a.	Right click Folders. > add connection
b.	Navigate to your cloned repository
c.	Hit ok
d.	Expand the newly connected repository. You should see the contents of the cloned repository listed in the contents pane.
4.	Next, In the ArcGIS Pro project, to open the Python window, on the Analysis tab, in the Geoprocessing group, click the drop-down menu under the Python button New Notebook and click the Python window button Show Python window.
5.	Right click in the python prompt section of the python window at the bottom and select ‘Load Code’
6.	Navigate to the Repository file path, and select ‘EGM722_AlexMason_B01039763_HLS_RAG_Assessment.py’
7.	The python window should be populated by the script.
8.	Check in the header rows that the variable home_folder is set to the file path of your repository. If not, overwrite it to be such.
9.	Put your cursor next to the final line of code, then hit return / enter. The script should run, giving a first message of ‘Running LULC Reclassification.’ Followed by several messages at the start and end of each function in the workflow. 
10.	The process may take a while, depending on the power of your machine. The slowest process is the Mosaic_DEM() function. The dialog will list the DEM tiffs held in your repository within /InputDataDEM.
11.	The script should run without issue. If necessary, follow the message outputs for any errors. Check relevant Esri documentation as a first pass. There should not be any errors if you have ArcGIS Pro installed appropriately and have access to Basic or Standard license, with the Spatial Analyst and 3D Analyst extensions active.
12.	Once run completely, you will receive the message: ‘Process finished successfully.’
13.	Check within your cloned directory that you have a new list of generated .tif files, including the final output files, also viewable in the Contents pane:
a.	outWeightedOverlayWildcat.tif
b.	outWeightedOverlayMerlin.tif
c.	outWeightedOverlayChinook.tif
14.	Arc will likely automatically add the 2m Slope and 2m DEM output files to any map window you may have open. You can remove these layers as they are not required.
15.	If completed successfully, you can close the Python window within the arc project.

How to run the script using Command Line:
To run the script outside of ArcGIS pro, users must still have the software installed. Follow the following advice within documentation Run stand-alone scripts—ArcGIS Pro | Documentation
1.	Open a windows Command Line instance.
2.	Set your Current Directory to the file path of the cloned repository.
a.	Use the command cd and copy the path of the directory. Hit enter / return.
3.	With the command line window showing your directory file path as the current directory, enter the following prompt:
a.	"C:\Program Files\ArcGIS\Pro\bin\Python\Scripts\propy" EGM722_AlexMason_B01039763_HLS_RAG_Assessment.py
4.	The script should begin running. After a few seconds, a message stating ‘Running LULC Reclassification’ should be shown, followed by a sequence of messages stating each step of the script has run successfully.
5.	Once the whole script has run, you should see a printed message stating ‘Process finished successfully.’
6.	Check the contents of your current directory, by typing the command dir
7.	You should now see a set of .tif files which comprise the outputs of the script.
8.	If file list is as expected, close the Command Line window.

How to display the data:
1.	Open an ArcGIS Pro project, add a folder connection to your repository file path, then insert new map.
2.	Within the map, Add Data > navigate to your repository, then within LayerFiles select the following three layer files (.lyrx):
a.	Weighted_Overlay_Chinook
b.	Weighted_Overlay_Merlin
c.	Weighted_Overlay_Wildcat
3.	Add all three layers to the map. The data link should be broken, denoted by a red exclamation mark next to the layer name.
4.	To repair the data sources, click on the first exclamation mark, which opens the ‘Repair data source’ dialogue window
5.	Navigate to your cloned repository location and select the corresponding outWeightedOverlay[HelicopterType].tif file. 
6.	Once complete for one, Arc should auto-repair connections to the other two. If it doesn’t, follow the above step and repeat for each of the remaining two geotiffs.
7.	You should be able to now see three semi-transparent layers covering your denoted AOI. Symbology should be based on ‘Probability Yardstick’ and display grey, red, amber or green colours.
