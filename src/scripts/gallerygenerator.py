import datetime
from pprint import pprint
from PIL import Image, ExifTags
import os
# import ffmpeg
import subprocess
import json
import random
# import geopy
# from geopy.geocoders import Nominatim
# from geopy.exc import GeocoderServiceError


# Get the list of all files and directories (so that they can all be uploaded to the gallery)

path = "./public/galleryPhotos"
dir_list = os.listdir(path)
# print("Files and directories in '", path, "' :")
# prints all files
# pprint(dir_list)


# Store more specific information about different images
# Name: [location, time, description

infodict = {
    # 'Zenith CH 750.jpg':                                        ['Bentonville, AR','',''],
    'Statue of Liberty.MOV':                                    ['New York City, NY','',''],
    'Daytime Flight.jpeg':                                      ['Crystal Lake, AR','',''],
    'Finished Zenith Rudder.JPG':                               ['Mexico, MO','',''],
    # 'Nick Akey Flying.JPG':                                     ['Bentonville, AR','',''],
    # 'Airplane Wing Spar.jpg':                                   ['Bentonville, AR','',''],
    'Will Rogers & Kate Chrisco on a Cross-Country Flight.jpeg':['Bentonville, AR','',''],
    'Will Rogers & Zachary Wagner.JPG':                         ['Mexico, MO','',''],
    'Skyhawk at Dusk.jpg':                                      ['Bentonville, AR','',''],
    'Zenith Rudder Clecoing.JPG':                               ['Mexico, MO','',''],
    'EAA Tools.jpg':                                            ['Manassas, VA','',''],
    'EAA Avionics Circuit Diagram.jpg':                         ['Manassas, VA','',''],
    'Nighttime Flight.jpeg':                                    ['Bentonville, AR','',''],
    'Zenith Rudder Riveting.mp4':                               ['Mexico, MO','',''],
    'Sunset in the Ozarks.jpeg':                                ['Bentonville, AR','',''],
    'Airplane Tail at Sunset.jpeg':                             ['Bentonville, AR','',''],
    # 'Airplane Window Overlooking the Atlantic Ocean.JPG':       ['Bentonville, AR','',''],
    'Taking Off From Grass.mov':                                ['Trigger Gap, AR','',''],
    'Atlantic Ocean.JPG':                                       ['New York City, NY','',''],
    # 'Nick Akey & Kiele Trainor.JPG':                            ['Bentonville, AR','',''],
    'EAA Avionics Trianing Kit.jpg':                            ['Manassas, VA','',''],
    'Will on a Cross country Flight.png':                        ['Bentonville, VA','',''],
}



totalString = ""
random.shuffle(dir_list)
for i in range(len(dir_list)):
    # print(i)
    sourcename = str(dir_list[i]) # date + name
    if sourcename == '.DS_Store':
        continue
    # print(sourcename)
    # link = "#"
    link = f"/galleryPhotos/{sourcename}"
    location = "Princeton, NJ"

    # TEMP (just because I am lazy)
    id = sourcename[:sourcename.rfind(".")] # ex: video.mp4->video
    description = id
    try:
        location = infodict[sourcename][0]
    except:
        print(id)
    

    # Grab date from meta data
    visual = str(sourcename[sourcename.rfind(".")+1:])
    if visual.lower() == "mov" or visual.lower() == "mp4":
        mediatag = f"""
                <video playsinline autoplay muted loop id="background-video">
                    <source src="/galleryPhotos/{sourcename}" type="video/mp4">
                    <source src="/galleryPhotos/{sourcename}" type="video/quicktime">
                    Your browser does not support the video tag.
                </video>
                """

        # # get metadata
        # vid = ffmpeg.probe(f"public/galleryPhotos/{sourcename}")
        # print(vid['streams'])

        # # Alt method
        # def get_video_metadata(path):
        #     result = subprocess.run(
        #         ["ffprobe", "-v", "error", "-show_entries",
        #         "format=duration:stream=width,height,codec_name,avg_frame_rate",
        #         "-of", "json", path],
        #         stdout=subprocess.PIPE,
        #         stderr=subprocess.STDOUT
        #     )
        #     return json.loads(result.stdout)

        # # Example usage
        # metadata = get_video_metadata("example.mp4")
        # print(json.dumps(metadata, indent=2))


        # # Alt Method
        # cap = cv2.VideoCapture("example.mp4")
        # width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        # height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        # fps = cap.get(cv2.CAP_PROP_FPS)
        # frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
        # duration = frame_count / fps

        # print("Resolution:", width, "x", height)
        # print("FPS:", fps)
        # print("Duration:", duration, "seconds")

        # cap.release()

        x = datetime.datetime.now()
        year = x.year
        month = x.month
        day = x.day
        # print(year, month, day)
        
    else:
        # <picture>
        #     <source srcset="https://gabriellew.ee/static/images/photography/2021-02-27-sunset.jpg, https://gabriellew.ee/static/images/photography/2021-02-27-sunset.jpg 2x" media="(max-width: 3000px)">
        #     <img src="https://gabriellew.ee/static/images/photography/2021-02-27-sunset.jpg" alt="">
        # </picture>

        img = Image.open(f"./public/galleryPhotos/{sourcename}")
        mediatag = f"""
                <picture>
                    <img src="/galleryPhotos/{sourcename}" alt="{description}">
                </picture>"""
        try:
            
            exif = { ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS }
            # pprint(exif)


            ## GET GPS INFO AUTOMATICALLY ##
            # gps = exif["GPSInfo"] # Just need North, east
            # north = gps[2]
            # east = gps[4]
            # Latitude =  (((north[0]*60) + north[1]*60)+north[2]) /60 /60
            # Longitude = (((east[0]*60) + east[1]*60)+east[2]) /60 /60

            # # Initialize Nominatim API with a more descriptive user agent
            # geolocator = Nominatim(user_agent="my_geopy_app")

            # # # Latitude & Longitude input
            # # Latitude = "25.594095"
            # # Longitude = "85.137566"

            # try:
            #     location = geolocator.reverse(Latitude + "," + Longitude)
            #     address = location.raw['address']

            #     # Traverse the data
            #     city = address.get('city', '')
            #     state = address.get('state', '')
    
            #     print('City : ', city)
            #     print('State : ', state)

            # except GeocoderServiceError as e:
            #     print("Error: ", e)


            
            # print(str(exif.get("DateTime")).replace(" ", ":").split(":")[:3])
            year, month, day  = map(int, str(exif.get("DateTime")).replace(" ", ":").split(":")[:3])
        except:
            x = datetime.datetime.now()
            year = x.year
            month = x.month
            day = x.day
            # print(year, month, day)


    # Alt Grab date from title
    # year, month, day  = map(int, id[:sourcename.rfind("-")].split("-")) # Example date in YYYYMMDD format
    timestamp = datetime.datetime(year, month, day)
    datetime_object = timestamp.strftime('%B %d, %Y')
    # datetime_object = datetime.datetime.strptime(date_str, "%Y%m%d")
    datetime_object = datetime_object[:datetime_object.find(" ")] +" "+ datetime_object.split()[1].lstrip("0") + datetime_object[datetime_object.rfind(" "):] 
    # print(datetime_object)



    # html for list item
    huhflea = f"""
            <li class="photo-grid-item">
                <figure>
                {mediatag}
                <figcaption>
                    <fieldset>
                    <input id="{sourcename}" type="checkbox">
                    <label class="photo-close" for="{sourcename}"></label>
                    <label class="photo-link" for="{sourcename}">
                        <svg class="icon" viewBox="0 0 100 100">
                        <circle cx="49" cy="49" r="36"></circle>
                        <path d="M45,69 L55,69 M45,39 L50,39 L50,69 M49.5,29 L50,29"></path>
                        </svg>
                    </label>
                    <dl>
                        <label for="{sourcename}">
                        <svg class="icon" viewBox="0 0 100 100">
                            <polyline points="14 32 50 68 86 32"></polyline>
                        </svg>
                        </label>
                        <div>
                        <dt>Date</dt>
                        <dd>{datetime_object}</dd>
                        </div>
                        <div>
                        <dt>Location</dt>
                        <dd>{location}</dd>
                        </div>
                        <div>
                        <dt>Description</dt>
                        <dd>{description}</dd>
                        </div>
                        <a class="photo-link" target="_blank" href="{link}" tabindex="-1">
                        <svg class="icon" viewBox="0 0 100 100">
                            <path d="M82,38 L82,78.9930191 C82,80.6537288 80.663269,82 78.9989882,82 L21.0010118,82 C19.3435988,82 18,80.663269 18,78.9989882 L18,21.0010118 C18,19.3435988 19.3408574,18 21.0069809,18 L62,18 M88.9559283,10.8111066 L57.9878833,42.132705 M69.2453268,10.8994949 L89.0443166,10.8994949 L89.0443166,30.6984848"></path>
                        </svg>
                        </a>
                    </dl>
                    </fieldset>
                </figcaption>
                </figure>
            </li>"""
    totalString += huhflea

base = """---
import { Image } from 'astro:assets';
import "../styles/global.css";
import "../styles/bullet.css";
import "../styles/gallery.css";
import Layout from "../layouts/Layout.astro";
const title = "Gallery";
---

<Layout pageTitle={title}>
    <main ontouchstart="true">
    <section class="photo-grid">
        <ul class="grid-isotope">
""" + totalString + """
        </ul>
    </section>
    </main>
</Layout>

"""


# print(totalString)
file_path = os.path.join(os.getcwd(), 'src', 'pages', 'gallery.astro')
print("Current working directory:", os.getcwd())
# os.truncate(file_path, 0)
# file = open("gallery.astro", "w")
with open(file_path, 'w') as file:
    file.write(base)