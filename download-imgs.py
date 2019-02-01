import urllib.request
import os

directory = "image-data-set"
if not os.path.exists("image-data-set"):
    os.makedirs(directory)

with open("open-images-dataset-train0.tsv") as ins:
    for line in ins:
        url = line.split()[0]
        file_name = url.split('/')[-1]
        path = str(os.path.join(directory, file_name))
        try:
            urllib.request.urlretrieve(url, path)
        except:
            print("")
        print(path)
