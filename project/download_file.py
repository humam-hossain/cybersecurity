import requests

def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name,"wb") as out_file:
        out_file.write(get_response.content)    

download("https://s.aolcdn.com/dims-global/dims3/GLOB/legacy_thumbnail/640x400/quality/80/https://s.blogcdn.com/slideshows/images/slides/728/890/2/S7288902/slug/l/01-2019-mercedes-amg-c63-ny-1.jpg")
