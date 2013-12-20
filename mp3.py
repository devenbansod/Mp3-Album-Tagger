from mutagen.easyid3 import EasyID3 as edit
import os,time
dirs = [d for d in os.listdir(os.getcwd()) if os.path.isdir(os.path.join(os.getcwd(),d))]
#for i in range(0,len(dirs)):
#      print dirs[i]
print "***Make sure you are in the folder containing FOLDERS of the Album-wise!***"
ans1=raw_input("***Rename the Album Folder with the Correct Name***\n***And Then Press Enter***")
#print os.getcwd()
for l in range(0,len(dirs)):
      b=dict();
      a= os.listdir(dirs[l]);
      ans2=raw_input("**You are in '"+dirs[l]+"' Folder**\n**All the Mp3s in this folder will be given the Album Name as '"+dirs[l]+"'\n**If You are ready to continue press Enter**")
      j=0
      os.chdir(dirs[l])
      for i in range(0,len(a)):
            if '.mp3' in a[i]:
              b[j]=a[i]
              j=j+1;
          
      if len(b)>0:
          print "The List of Mp3s that will be changed are :";
          for i in range(0,len(a)):
            if '.mp3' in a[i]:
              print a[i]+"\n"
              b[j]=a[i]
              j=j+1;
          
          print "All the above listed mp3s Will be changed as\n**Mp3 Album : '"+dirs[l]+"'**";
          ans3=raw_input("If you are ready, Please enter 'Y' and Press 'Enter'");
          if ans3=='Y':
            for i in range(0,j-1):
              audio = edit(b[i])
              audio['album'] = dirs[l];
              audio.save()
            print "All Done!!"
          else:
            print "Nothing Changed in this Folder!!!\nMoving Forward!!"
            time.sleep(5)
      else :
        print "No Mp3 File Found in the Folder"
      time.sleep(10)
      os.chdir("./..")
