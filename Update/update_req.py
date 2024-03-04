import requests
import json
import zipfile
import os


GITHUB_REPO = "https://api.github.com/repos/onehitto/2D_CNC_plotter/releases"


class app_def:
    config_file ='.\\cache\\config.json'
    versiondumpfile = ".\\cache\\versiondumpfile.json"
    
    def __init__(self):
        cache_dir = os.path.dirname(self.versiondumpfile)
        if not os.path.exists(cache_dir):
            os.makedirs(cache_dir)
        self.config =''
        self.get_current_version()
        self.get_versions()
    
    def get_versions(self):
        self.versions = []
        try: 
            response = requests.get(GITHUB_REPO)
            if response.status_code == 200:
                for version_data in response.json():
                    version_info = {
                    "tag_name": version_data['tag_name'],
                    "exe_url": f"https://github.com/onehitto/2D_CNC_plotter/releases/download/{version_data['tag_name']}/2D.exe",
                    "name": version_data['name'],
                    "link": version_data['html_url']}
                    self.versions.append(version_info)
                    
                with open(self.versiondumpfile, 'w') as f:
                    json.dump(self.versions, f, indent=4)
        except requests.RequestException as e:
            print(f"An error occurred: {e}")
    def get_current_version(self):
        rt = '0'
        try:
            with open(self.config_file, 'r') as f:
                self.config = json.load(f)
            rt = self.config['settings']['current_version'] 
        except FileNotFoundError:
            self.config ={"settings":{'current_version' : "0"}}
            print("Error: 'config.json' not found.")

    def download_file(self,url, local_filename):
    # Send a GET request to the URL
        with requests.get(url, stream=True) as r:
            # Raise an HTTPError for bad responses
            r.raise_for_status()
            # Open the local file for writing in binary mode
            with open(local_filename, 'wb') as f:
                # Iterate over the response data in chunks
                for chunk in r.iter_content(chunk_size=8192):
                    # Write the chunk to the file
                    f.write(chunk)

    def check_for_updates(self):
        current_version = self.config['settings']['current_version']           
        if current_version != self.versions[0]['tag_name']:
            print(f"Update available: {self.versions[0]['tag_name']}")
            #print(f"Download URL: {versions[0]['exe_url']}")
            self.config['settings']['current_version'] = self.versions[0]['tag_name']
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=4)
            #self.download_file(versions[0]['exe_url'],".\\cache/2D.exe")
            #os.replace(".\\cache/2D.exe",".\\2D.exe")
            
            """with zipfile.ZipFile(".\\cache/update.zip", 'r') as zip_ref:
                zip_ref.extractall(".\\cache")
            os.remove(".\\cache/update.zip")"""
        return False, None, None
"""
        needs_update, latest_version, download_url = check_for_updates()
        if needs_update:
            print(f"Update available: {latest_version}")
            print(f"Download URL: {download_url}")
            # Here you can add code to download and apply the update
        else:
            print("Your application is up to date.")"""
        

