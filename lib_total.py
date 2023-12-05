import requests
import wget
import os
import subprocess 
import urllib.request, json 
import shutil 

url = 'http://gibhubfonts.atwebpages.com/task/download/cap_online.html'
url = 'https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/116.0.5845.96/win32/chrome-win32.zip'




####===================== FILE RELATE ================================####

def task_download(code): 
   url        = code['url_from']
   file_local = code['url_to']
   method     = code['method']
   if method == 'request': 
      response = requests.get(url)
      open(file_local, "wb").write(response.content) 
    
   if method == 'wget' : 
      response = wget.download(url, file_local)

   if method == 'urllib' : 
       response = urllib.request.urlretrieve(url, file_local)



def delete_file(file_url): 
    if os.path.exists(file_url):
       os.remove(file_url)
    else:
       print("The file does not exist")



def update_local_file(local_file_name,data_input):
    with open(local_file_name,'w') as f:
        f.write(data_input)
        f.close()
        


def read_json_file(json_file_name):
    url_server =  urllib.request.urlopen(json_file_name)
    data_server = json.loads(url_server.read().decode())
    return data_server
        
def read_local_file(local_file_name):
    folder_file = open (local_file_name, "r")
    data_file   = folder_file.read()
    folder_file.close()
    return data_file


def copy_file(source,destination,method):
    if method == 'copyfile' : 
        shutil.copyfile(source,destination)
    
    if method == 'copy' : 
       shutil.copy(source,destination)
       
    if method == 'copy2' : 
        shutil.copy2(source,destination)
    

        

def task_copy(data):
    method    = data['method']
    url_from  = data['url_from']
    url_to    = data['url_to'] 
        
    if method == 'copyfile' : 
        shutil.copyfile(url_from,url_to)
    
    if method == 'copy' : 
       shutil.copy(url_from,url_to)
       
    if method == 'copy2' : 
        shutil.copy2(url_from,url_to)

###===================================================================####




####===================== FOLDER RELATE ================================####
def delete_folder(path_delete):
    isExist = os.path.exists(path_delete)

    if isExist:
        try:
            shutil.rmtree(path_delete)
        except OSError as e:
            print ("Error: %s - %s." % (e.filename, e.strerror))

def make_folder(path_folder_parent,folder_name):
    path_folder  = path_folder_parent + '/' + folder_name
    check_exit_folder = os.path.exists(path_folder)
    
    if check_exit_folder:
        print(f'''Path: {path_folder } : done''')
    else: 
        print(f'''Make Folder: {path_folder }''')
        os.makedirs(path_folder)
    return path_folder

###===================================================================####





###======================== TASK RELATE ===============================####
def cmd_request(content):
    ### update time request to local file 
    
    ### Apply request 
    try : 
      subprocess.run(content,shell=True,check=True)
    except : 
        pass


def update_time_request(time_request) : 
    file_name = 'task_time.txt' 
    try : 
       update_local_file(file_name,time_request)
    except : 
        pass



def run_task_all(task): 
    task_name = task['task']
    if task_name == 'cmd' : 
        print('cmd code run')
        cmd_code = task['code']
        cmd_request(cmd_code)
        
    if task_name == 'copy':
        copy_code = task['code']
        task_copy(copy_code)
    
    if task_name == 'download':
        download_code = task['code'] 
        task_download(download_code)
        
###==========================: 




# ==========================================####


# data = read_json_file('http://gibhubfonts.atwebpages.com/app/task/genba.json')
# print(data)



# copy_file('D:/02.MAS/0.149/034_230808192036_6007_ff.mp4','T:/3.Task/02-IMAGE/lib/test.mp4','copy')
# delete_file('T:/3.Task/02-IMAGE/lib/test.mp4')