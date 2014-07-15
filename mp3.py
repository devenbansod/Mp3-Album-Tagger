# This script edits the MP3 IDE3 Tags like Album, Artist etc.
# To be used in an ALBUM-WISE SORTED FOLDER of MP3s


# The NECESSARY Library for the Exceution
from mutagen.easyid3 import EasyID3 as edit

import os,time


dirs  =  [d for d in os.listdir(os.getcwd()) if os.path.isdir(os.path.join(os.getcwd(),d))]

# Prints Warning and Takes in Confirmation
print "***Make sure you are in the folder containing FOLDERS of the Album-wise!***"
ans1  =  raw_input("***Rename the Album Folder with the Correct Name***\n***And Then Press Enter***")


for l in range(0,len(dirs)):
      list_of_mp3s  =  dict();
      # Get an array of all Files in the this Folder
      list_of_files  =  os.listdir(dirs[l]);
      ans2  =  raw_input("**You are in '"  +   dirs[l]  +   "' Folder**\n**All the Mp3s in this folder will be given the Album Name as '" +  dirs[l] +  "'\n**If You are ready to continue press Enter**")
      j  =  0
      
      # Change to the dirs[l] directory 
      os.chdir(dirs[l])
      
      for i in range(0,len(list_of_files)):
            # If an MP3 is found, please append its name in a different Dictionary
            if '.mp3' in list_of_files[i]: 
              list_of_mp3s[j] = list_of_files[i]
              j = j +  1;
          
      if len(list_of_mp3s)>0:
            # Print all the MP3s that will be Modified
          print "The List of Mp3s that will be changed are :";
          for i in range(0,len(list_of_files)):
            if '.mp3' in list_of_files[i]:
              print list_of_files[i] +  "\n"
              list_of_mp3s[j] = list_of_files[i]
              j = j +  1;
          
          # Take a Confirmation reagarding the Modification of the MP3s
          print "All the above listed mp3s Will be changed as\n**Mp3 Album : '" +  dirs[l] +  "'**";
          ans3 = raw_input("If you are ready, Please enter 'Y' and Press 'Enter'");
          
          # If confirmed, change the Album TAG of all the Listed MP3s to Folder name
          if ans3 =  = 'Y':
            for i in range(0,j-1):
              audio  =  edit(list_of_mp3s[i])
              audio['album']  =  dirs[l];
              audio.save()
            print "All Done!!"
            
          # If not confirmed, leave all as it is
          else:
            print "Nothing Changed in this Folder!!!\nMoving Forward!!"
            time.sleep(5)
      else :
        print "No Mp3 File Found in the Folder"
      time.sleep(10)
      
      # Again move back to Parent Directory 
      os.chdir("./..")
