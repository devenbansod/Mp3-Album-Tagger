from mutagen.easyid3 import EasyID3 as edit
import os,time;
b=dict();
ans1=raw_input("***Make sure you are in the folder containing the Mp3s of that Album!***\n***Rename the Album Folder with the Correct Name***\n***And Then Press Enter***")
cwd=os.getcwd().split("\\")
a= os.listdir(os.getcwd());
ans2=raw_input("**You are in '"+cwd[-1]+"' Folder**\n**All the Mp3s in this folder will be given the Album Name as '"+cwd[-1]+"'\n**If You are ready to continue press Enter**")
j=0
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
    
    print "All the above listed mp3s Will be changed as\n**Mp3 Album : '"+cwd[-1]+"'**";
    ans3=raw_input("If you are ready, Please enter 'Y' and Press 'Enter'");
    if ans3=='Y':
      for i in range(0,j-1):
        audio = edit(b[i])
        audio['album'] = cwd[-1];
        audio.save()
      print "All Done!!"
    else:
      print "Nothing Changed!!!\nEXITING!!"
      time.sleep(5)
      exit()
else :
  print "No Mp3 File Found in the Folder"
time.sleep(10)
