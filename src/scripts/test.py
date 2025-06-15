import os
path = "./public/galleryPhotos"
dir_list = os.listdir(path)
for i in range(len(dir_list)):
    # print(i)
    sourcename = str(dir_list[i]) # date + name
    if sourcename == '.DS_Store':
        continue
    print(f"'{sourcename}':".ljust(60) +  "['Bentonville, AR','',''],")