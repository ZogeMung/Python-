import requests
loop = 1
chapters = 1
sessions = 1
pages = 1
def DownloadPic(imgByte):
    f = open('./alg2_%02d_%02d_p%03d.png' %(chapters, sessions, pages), 'wb')
    f.write(imgByte)
    f.close()
while loop:
    url = 'https://bim.easyaccessmaterials.com/protected/content/dcs_cc3/alg2/c%02d/%02d/alg2_%02d_%02d_p%03d.png' %(chapters, sessions, chapters, sessions, pages)
    obj = requests.get(url)
    if obj.status_code == 200:  #Chapter read successful
        while loop:
            url = 'https://bim.easyaccessmaterials.com/protected/content/dcs_cc3/alg2/c%02d/%02d/alg2_%02d_%02d_p%03d.png' %(chapters, sessions, chapters, sessions, pages)
            obj = requests.get(url)
            if obj.status_code == 200:  #Session read successful
                while loop:
                    url = 'https://bim.easyaccessmaterials.com/protected/content/dcs_cc3/alg2/c%02d/%02d/alg2_%02d_%02d_p%03d.png' %(chapters, sessions, chapters, sessions, pages)
                    obj = requests.get(url)
                    if obj.status_code == 200:  #Page read successful
                        print('Downloading... alg2_%02d_%02d_p%03d.png' %(chapters, sessions, pages))
                        DownloadPic(obj.content)
                        pages += 1
                    else:   #Next session
                        sessions += 1
                        pages = 1
                        break
            else:   #Next chapter
                chapters += 1
                sessions = 1
                pages = 1
                break
    else:   #End
        break
print('Completed!')
