
import zipfile, sys, os, glob  
 #------------------------------------------------------------   
def zipTiffFilesInDir(inDir, outDir):  
    # Check that input directory exists  
    if not os.path.exists(inDir):  
        print ("Input directory %s does not exist!" % inDir)
        return False  
  
    # Check that output directory exists  
    if not os.path.exists(outDir):  
        # Create it if it does not  
        print ("Creating output directory %s" %outDir)
        os.mkdir(outDir)  
  
    print ("Zipping tiffFile(s) in folder %s to output folder %s" % (inDir, outDir)) 
  
    # Loop through tif-files in input directory  
    for inTiff in glob.glob(os.path.join(inDir, "*.tif")):  
        # Build the filename of the output zip file  
        outZip = os.path.join(outDir, os.path.splitext(os.path.basename(inTiff))[0] + "_tiff_v1.zip")  
  
        # Zip the tifffile  
        zipTiffFile(inTiff, outZip)  
    return True 
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
        outZip = os.path.join(outDir, os.path.splitext(os.path.basename(inShp))[0] + "_shp_v1.zip")  
  
        # Zip the shapefile  
        zipShapefile(inShp, outZip)  
    return True     
#------------------------------------------------------------  
def zipTiffFile(intifffile, newZipFN):  
    print ('Starting to Zip '+(intifffile)+' to '+(newZipFN))
  
    # Check that input tif-file exists  
    if not (os.path.exists(intifffile)):  
        print (intifffile + ' Does Not Exist')
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
  
    # Loop through tifffile components  
    for infile in glob.glob( intifffile.lower().replace(".tif",".*")):  
        # Skip .zip file extension  
        if os.path.splitext(infile)[1].lower() != ".zip":  
            print ("Zipping %s" % (infile))  
            # Zip the tifffile component  
            zipobj.write(infile,os.path.basename(infile),zipfile.ZIP_DEFLATED)  
  
    # Close the zip file object  
    zipobj.close()  
    return True  
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
    # Main method, used when this script is the calling module, otherwise  
    # you can import this module and call your functions from other modules  
if __name__=="__main__":  
    ##    testtifffile = r"C:\temp\geomTest.shp"  
    ##    testZipFile = r"C:\temp\geomTest.zip"  
    ##    zipTiffFile(testtifffile,testZipFile)
    # Before edit
    #   inDir = r"c:\temp"  
    #   outDir = r"c:\temp\testZipShp"  
    #   zipTiffFilesInDir(inDir, outDir)  
    #   print "done!"
#------------------------------------------------------------      
    # NAIROBI FOLDERS
##    inDir = r"M:\Shared255\IDEAMAPS\WP_3\Nairobi_Updated"  
##    outDir = r"M:\Shared255\IDEAMAPS\WP_3\analysis_for_geoserver_godwin\zipped_files\nairobi_zipped_files_v2"  
##    zipTiffFilesInDir(inDir, outDir)  
##    zipShapefilesInDir(inDir, outDir)  
##    print ("done!")

    # LAGOS FOLDERS
##    inDir = r"M:\Shared255\IDEAMAPS\WP_3\Lagos_Updated"  
##    outDir = r"M:\Shared255\IDEAMAPS\WP_3\analysis_for_geoserver_godwin\zipped_files\lagos_zipped_files_v3"  
##    zipTiffFilesInDir(inDir, outDir)  
##    zipShapefilesInDir(inDir, outDir)  
##    print ("done!")
    
    # ACCRA FOLDERS
##    inDir = r"M:\Shared255\IDEAMAPS\WP_3\Accra_Updated"  
##    outDir = r"M:\Shared255\IDEAMAPS\WP_3\analysis_for_geoserver_godwin\zipped_files\Accra_zipped_files_v3"  
##    zipTiffFilesInDir(inDir, outDir)  
##    zipShapefilesInDir(inDir, outDir)  
##    print ("done!")

    # GLOBAL FOLDERS
      inDir = r"M:\Shared255\IDEAMAPS\WP_3\Global_Updated"  
      outDir = r"M:\Shared255\IDEAMAPS\WP_3\analysis_for_geoserver_godwin\zipped_files\global_zipped_files_v1"  
      zipTiffFilesInDir(inDir, outDir)  
      zipShapefilesInDir(inDir, outDir)  
      print ("done!")
 #------------------------------------------------------------  



#------------------------------------------------------------   
# Disclaimer: Modified from original at https://community.esri.com/thread/28985. Contribution: appending a '_v1' to zipped file.
