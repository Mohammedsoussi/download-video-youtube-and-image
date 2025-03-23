#for import package for use it
import requests
from pytubefix import YouTube
from tqdm import tqdm, trange
from time import sleep
import logging
import os 

#more information about your target video or audio or image
url_file = input('Please enter the url file :')
name_file = input('Please enter the name file :')
extension_file = input('Please enter the extension file :')
if extension_file not in ['jpeg', 'jpg', 'png', 'gif', 'mp3', 'WAV', 'AAC', 'M4A', 'WMA', 'mp4', 'WMV', 'MKV'] :
       print(f'[-]The is extension {extension_file} not available!')
       exit()

#To suppress errors that will be printed
logger = logging.getLogger('pytubefix').setLevel(logging.ERROR)


def downloads_file(url_file ,name_file, extension_file):
   #downloads image and gift with requests
    if extension_file in ['jpeg', 'jpg', 'png', 'gif'] :
      with requests.get(url_file, stream = True) as file :
         with open(name_file + '.' + extension_file, 'wb') as name_file :
             for chunk in file.iter_content(chunk_size = 16*1024) :
                name_file.write(chunk)
             for line in tqdm(range(100), unit='line', desc='Loading '):
                sleep(0.01)
             sleep(2.5)
             path = os.path.join('C:\\Users\Lenovo ThinkPad\\',name_file,'.',extension_file)
             if os.path.getsize(path) == 0:
                print("[-] Failed to downloads you target image, please try again")
             else:
                print('[+] Downloads completed was successufly')
    # this for download videos in youtube highest resolution
    elif extension_file in ["mp4"] :
         yt = YouTube(url_file, 'WEB')
         print("[+]Please wait for Downloading the video file ")
         ys = yt.streams.get_highest_resolution()
         total_size = ys.filesize
         name_file = ys.title
         with tqdm(total=total_size, unit='bytes', unit_scale=True, desc='Loading') as pbar:
           for i in trange(total_size) :
            pbar.update(1024)
           ys.download()
         if os.path.getsize(f'C:\\Users\\Lenovo ThinkPad\\{name_file}.mp4') == 0:
            print("[-] Failed to downloads you target image, please try again")
         else:
            print('[+] Downloads completed was successufly')
    else:
       print(f"your extention not found {extension_file}")
       help = input("if you want to see extention found now enter y if dont enter n")
       if help == "y":
          print("extension available now is :\nmp4, jpeg, jpg, png, gif")
 #the is for process errors      
try:
   downloads_file(url_file, name_file, extension_file)
except Exception as e :
   print(f'[-]We detecte an error:{e} ,Please try again!')