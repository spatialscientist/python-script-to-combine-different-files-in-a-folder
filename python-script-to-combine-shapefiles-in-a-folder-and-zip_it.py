# Pyton script for zipping ESRI Shapefiles and appending a version number to the zipped folder
# Disclaimer: Modified from original at https://community.esri.com/thread/28985. 

import zipfile, sys, os, glob  
 #------------------------------------------------------------   
##def zipTiffFilesInDir(inDir, outDir):  
##    # Check that input directory exists  
##    if not os.path.exists(inDir):  
##        print ("Input directory %s does not exist!" % inDir)
##        return False  
##  
##    # Check that output directory exists  
##    if not os.path.exists(outDir):  
##        # Create it if it does not  
##        print ("Creating output directory %s" %outDir)
##        os.mkdir(outDir)  
##  
##    print ("Zipping tiffFile(s) in folder %s to output folder %s" % (inDir, outDir)) 
##  
##    # Loop through tif-files in input directory  
##    for inTiff in glob.glob(os.path.join(inDir, "*.tif")):  
##        # Build the filename of the output zip file  
##        outZip = os.path.join(outDir, os.path.splitext(os.path.basename(inTiff))[0] + "_tiff_v2.zip")  
##  
##        # Zip the tifffile  
##        zipTiffFile(inTiff, outZip)  
##    return True 
#------------------------------------------------------------  
def zipShapefilesInDir(inDir, outDir):  
    # Check that input directory exists  
    if not os.path.exists(inDir):  
        print ("Input directory %s does not exist!" % inDir)
        return False  
  
    # Check that output directory exists  
    if not os.path.exists(outDir):  
        # Create it if it does not  
        print ("Creating output directory %s" %outDir)
        os.mkdir(outDir)  
  
    print ("Zipping shapefile(s) in folder %s to output folder %s" % (inDir, outDir)) 
  
    # Loop through shapefiles in input directory  
    for inShp in glob.glob(os.path.join(inDir, "*.shp")):  
        # Build the filename of the output zip file  
        outZip = os.path.join(outDir, os.path.splitext(os.path.basename(inShp))[0] + "_shp_v2.zip")  
  
        # Zip the shapefile  
        zipShapefile(inShp, outZip)  
    return True     
#------------------------------------------------------------  
##def zipTiffFile(intifffile, newZipFN):  
##    print ('Starting to Zip '+(intifffile)+' to '+(newZipFN))
##  
##    # Check that input tif-file exists  
##    if not (os.path.exists(intifffile)):  
##        print (intifffile + ' Does Not Exist')
##        return False  
##  
##    # Delete output zipfile if it already exists  
##    if (os.path.exists(newZipFN)):  
##        print ('Deleting '+newZipFN)
##        os.remove(newZipFN)  
##  
##    # Output zipfile still exists, exit  
##    if (os.path.exists(newZipFN)):  
##        print ('Unable to Delete'+newZipFN)  
##        return False  
##  
##    # Open zip file object  
##    zipobj = zipfile.ZipFile(newZipFN,'w')  
##  
##    # Loop through tifffile components  
##    for infile in glob.glob( intifffile.lower().replace(".tif",".*")):  
##        # Skip .zip file extension  
##        if os.path.splitext(infile)[1].lower() != ".zip":  
##            print ("Zipping %s" % (infile))  
##            # Zip the tifffile component  
##            zipobj.write(infile,os.path.basename(infile),zipfile.ZIP_DEFLATED)  
##  
##    # Close the zip file object  
##    zipobj.close()  
##    return True  
#------------------------------------------------------------  
def zipShapefile(inShapefile, newZipFN):  
    print ('Starting to Zip '+(inShapefile)+' to '+(newZipFN))
  
    # Check that input shapefile exists  
    if not (os.path.exists(inShapefile)):  
        print (inShapefile + ' Does Not Exist')  
        return False  
  
    # Delete output zipfile if it already exists  
    if (os.path.exists(newZipFN)):  
        print ('Deleting '+newZipFN)  
        os.remove(newZipFN)  
  
    # Output zipfile still exists, exit  
    if (os.path.exists(newZipFN)):  
        print ('Unable to Delete'+newZipFN)  
        return False  
  
    # Open zip file object  
    zipobj = zipfile.ZipFile(newZipFN,'w')  
  
    # Loop through shapefile components  
    for infile in glob.glob( inShapefile.lower().replace(".shp",".*")):  
        # Skip .zip file extension  
        if os.path.splitext(infile)[1].lower() != ".zip":  
            print ("Zipping %s" % (infile))  
            # Zip the shapefile component  
            zipobj.write(infile,os.path.basename(infile),zipfile.ZIP_DEFLATED)  
  
    # Close the zip file object  
    zipobj.close()  
    return True  
#------------------------------------------------------------   
    # FOLDERS
    inDir = r"Drive letter here:\your folder containing files here"  
    outDir = r"Drive letter here:\your output folder here"  
    #zipTiffFilesInDir(inDir, outDir)  
    zipShapefilesInDir(inDir, outDir) 
    print "done!"
#------------------------------------------------------------   
