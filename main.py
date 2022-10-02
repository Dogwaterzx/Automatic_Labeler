# Functions to get Google Vision API labels for an image
import json
from urllib import request

# returns list of strings (labels) parsed from result
def get_labels(result): 
  labels = []
  label_annotations = result["responses"][0]["labelAnnotations"]
  for a in label_annotations: 
    l = a['description']
    labels.append(l)
  return labels

################
# get_api_labels() function
# returns list of API labels for an image 
################3
def get_api_labels(image_url):

  # url for Google Vision API 
  api_url = "https://content-vision.googleapis.com/v1/images:annotate?key=AIzaSyAa8yy0GdcGPHdtD083HiGGx_S0vMPScDM"

  # data for request (Python dictionary) 
  request_data = {
          "requests": [
              {
                  "image": {
                      "source": {
                          "imageUri": image_url
                      }
                  },
                  "features": [{"type": "LABEL_DETECTION"}, {"type": "WEB_DETECTION"}],
              }
          ]
      }

  # json.dumps() converts Python object into JSON 
  json_data = json.dumps(request_data)

  # create new Request object
  req = request.Request(
      api_url,
      json_data.encode("utf-8"),
      {
          "Content-Type": "application/json",
          "x-referer": "https://explorer.apis.google.com",
      },
  )

  # open Request and get a response from API (HTTPResponse object)
  response = request.urlopen(req)
  
  # read JSON data from API response into result variable
  result_json = response.read()

  # json.loads() converts JSON data into Python dictionary
  result = json.loads(result_json.decode("utf8"))     

  # get list of labels from result 
  labels = get_labels(result)
  return labels


##################
# show_image() function shows an image on the screen.
#################
from PIL import Image
import requests
import matplotlib.pyplot as plt

def show_image(image_url):
  response = requests.get(image_url, stream=True)
  img = Image.open(response.raw)
  plt.axis('off')
  plt.imshow(img)
  plt.show()
