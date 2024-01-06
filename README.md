# Face recognition 
is a project for the goal of is to detect face id from a custom image and secure access for a specific data inside a folder in the Desktop, and the only way to access the data is after face verification from the webcam.
# file description
**Image Folder** Contain image of the faces that should have access to the secure folder,<br>
**faces.json** Contain the description for the images inside **Image Folder** <br>
**with this format "Name" : "image_path"**<br><br>
**file_path.json** Contain the path for the folder that should be secure<br>
**file_path.py** Contain the scipt that change the folder path<br><br>
**crypt.py** Contain the script that crypt all data in a folder<br>
**decrypt.py** Contain the script that decrypt all data in a folder<b><br>
**face_detect.py** Contain the code that open webcam and detect face id and check if face id match or not, <br>
if is match then run the decrypt script, else run the crypt script . <br><br>
**main.py** run the application <br><br>
with this commend : `python3 main.py` for linux <br>
and : `python main.py` for windows<br><br><br>
**warning !!  you need to install some package to run the application, you can found them in recommended file**



