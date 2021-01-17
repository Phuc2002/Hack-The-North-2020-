
import Algorithmia

def split_video():
    #classname = input("Enter your class name: ")
    #lecturename = input("Enter your lecture #: ")
    input = {
      "format": "SplitToSubvideos",
      "data": {
          "input": {
              "inputVideoUrl": "data://Chillies/tmp/Video.mp4"
        },
          "output": {
              "collection": "data://.algo/perm",
              "prefix": "test",
              "extension": "mp4",
              "zippedOutput": False
        }
      }
    }

    client = Algorithmia.client('<API-KEY>')
    algo = client.algo('media/VideoAlgorithms/0.2.5')
    algo.set_options(timeout=300) # optional
    result = algo.pipe(input).result
    print("Spliting successful")

#split_video()
