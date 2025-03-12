import os
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaFileUpload


class GoogleDriveApi:
    _CLIENT_SECRET_FILE = 'credentials.json'
    _API_NAME = 'drive'
    _API_VERSION = 'v3'
    _SCOPES = ['https://www.googleapis.com/auth/drive']


    def __init__(self):
            self.__drive_service = self.__authenticate_google_drive()

    
    def __authenticate_google_drive(self):
        creds = None

        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    self._CLIENT_SECRET_FILE, self._SCOPES)
                creds = flow.run_local_server(port=0)
        
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        
        service = build(self._API_NAME, self._API_VERSION, credentials=creds)
        return service
    

    def search_folder(self, folder_name):
        query = f"name='{folder_name}' and mimeType='application/vnd.google-apps.folder'"
        results = self.__drive_service.files().list(q=query, fields="files(id, name)").execute()
        folders = results.get('files', [])
        if folders:
            print(f"Folder '{folder_name}' Already Exists - Folder ID: {folders[0]['id']}")
            return folders[0]['id']
        else:
            return None


    def create_folders(self, folder_name):

        folder_id = self.search_folder(folder_name)
        if folder_id:
            return folder_id

        file_metadata = {
            'name': folder_name,
            'mimeType': 'application/vnd.google-apps.folder'
            }

        folder = self.__drive_service.files().create(body=file_metadata, fields='id').execute()
        print(f"Folder created: {folder_name}, Folder ID: {folder['id']}")
        return folder['id']


    def upload_file(self, file_name, file_path, mime_type, folder_id):
    
        file_metadata = {'name': file_name, 
                        'parents': [folder_id]}
        media = MediaFileUpload(file_path, mimetype=mime_type)
        
        file = self.__drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        print(f"File uploaded successfully, File Folder ID: {file['id']}")
        return file['id']
    

    def download_file(self, file_id, file_name):
        request = self.__drive_service.files().get_media(fileId=file_id)
        with open(file_name, 'wb') as f:
            downloader = request.execute()
            f.write(downloader)
        print(f"File {file_name} downloaded successfully!")


    def delete_file(self, file_id):
        try:
            self.__drive_service.files().delete(fileId=file_id).execute()
            print(f"File with ID {file_id} deleted successfully.")
        except Exception as e:
            print(f"An error occurred: {e}")


    def search_files(self, folder_id):
        query = f"'{folder_id}' in parents and mimeType!='application/vnd.google-apps.folder'"
        results = self.__drive_service.files().list(q=query, fields="files(id, name)").execute()
        files = results.get('files', [])
        if files:
            print("Files in Folder:")
            for file in files:
                print(f"Found File Name: {file['name']} - File ID: {file['id']}")
        else:
            print("Folder is Empty!")


    def list_all_files(self):
        result = self.__drive_service.files().list(fields='files(id, name)').execute()
        files = result.get('files', [])
        if files:
            print("All Files in Google Drive:")
            for file in files:
                print(f"Name: {file['name']} - ID: {file['id']}")
        else:
            print("Google Drive is Empty!")


    def download_folder(self, folder_id, folder_name):
        query = f"'{folder_id}' in parents"
        results = self.__drive_service.files().list(q=query, fields="files(id, name)").execute()
        files = results.get('files', [])

        if not files:
            print(f"Folder '{folder_name}' is Empty")
            return

        folder_path = f"downloaded_files/{folder_name}"
        os.makedirs(folder_path, exist_ok=True)

        print(f"Downloading Folder: {folder_name}")

        for file in files:
            file_id = file['id']
            file_name = file['name']
            file_path = os.path.join(folder_path, file_name)

            request = self.__drive_service.files().get_media(fileId=file_id)
            with open(file_path, 'wb') as f:
                downloader = request.execute()
                f.write(downloader)
            print(f"{file_name} Downloaded Successfully")

        print(f"Folder '{folder_name}' Download Completed")


gda = GoogleDriveApi()


folder_name = 'Html5'
folder_id = gda.create_folders(folder_name)


mime_type = 'image/jpeg'
file_name = 'python.jpg'
file_path = 'crd/python.jpg'
file_id = gda.upload_file(file_name, file_path, mime_type, folder_id)


file_idz = '147kv0z1yVMnxNNFxQ0c9_O-2JuFlII28'
gda.download_file(file_idz, "downloadingFile.jpg")


file_idd = '1iXV4dwNcGB3h5uhJTevT86lB4Xw1Gy29'
gda.delete_file(file_idd)


gda.search_files(folder_id)

gda.list_all_files()

gda.download_folder(folder_id, folder_name)