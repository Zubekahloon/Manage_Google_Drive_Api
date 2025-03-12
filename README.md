# Google Drive Api File Manager

## Project Description
This Python-based project interacts with Google Drive API to manage files and folders directly from your local system. It provides a seamless way to upload, download, delete, search, and list files & folders using Python.

## Features
✔️ Authenticate & connect to Google Drive
✔️ Create folders in Google Drive
✔️ Upload files to a specific folder
✔️ Download files from Google Drive
✔️ Delete files from Google Drive
✔️ Search for files & folders
✔️ List all files in a folder or across Drive
✔️ Download entire folders

## Installation & Setup
### 🔹 Prerequisites
1️⃣ Install Python 3.x
2️⃣ Install required dependencies:
    pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
3️⃣ Enable Google Drive API & obtain credentials.json:
  Go to Google Cloud Console
  Enable Google Drive API
  Download credentials.json and place it in the project directory

### 🔹 Clone the Repository
git clone https://github.com/ZubeKahloon/Manage_Google_Drive_Api.git
cd Manage_Google_Drive_Api

### Run the Script
python filename.py

## Usage Guide
Once the script is running, you can perform various file management tasks.
1. Creating a Folder in Google Drive

folder_name = 'MyFolder'
folder_id = gda.create_folders(folder_name)

2. Uploading a File
   
file_name = 'example.jpg'
file_path = 'path/to/example.jpg'
mime_type = 'image/jpeg'
gda.upload_file(file_name, file_path, mime_type, folder_id)

3. Downloading a File

file_id = 'your_file_id_here'
gda.download_file(file_id, "downloaded_file.jpg")

4. Deleting a File

file_id = 'your_file_id_here'
gda.delete_file(file_id)

5. Searching for Files
 
gda.search_files(folder_id)

6. Listing All Files in Google Drive

gda.list_all_files()

7. Downloading an Entire Folder

gda.download_folder(folder_id, 'MyFolder')

## Example Output
✅ Folder 'Html5' Created - Folder ID: XXXXXX
✅ File uploaded successfully, File ID: YYYYYY
✅ File downloadingFile.jpg downloaded successfully!
✅ File with ID ZZZZZZ deleted successfully.
 Files in Folder:
 - example.jpg (ID: ABC123)
 All Files in Google Drive:
 - example.jpg (ID: ABC123)
 Folder 'Html5' Download Completed

##  Technologies Used
🔹 Python
🔹 Google Drive API
🔹 OAuth 2.0 Authentication
🔹 Pickle for Credential Storage

## Contributing
 Contributions are welcome! Feel free to fork this repository and submit a pull request with improvements or bug fixes.

##  Author & Contact
 Developed by Zube
 GitHub: ZubeKahloon

