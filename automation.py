import cv2
import time
import dropbox

start_time = time.time()

def take_Snapshot():
    print("SMILE FOR THE CAMERA")
    video_capture = cv2.VideoCapture(0)
    result = True
    while result:
        frame = video_capture.read()
        cv2.imwrite("img1.jpg",frame)
        result = False

    print("PICTURE TAKEN")
    video_capture.release()
    cv2.destroyAllWindows()

def upload_files(image_name):
    access_token = 'YhaAh8wcrQEAAAAAAAAAAQDal5GIVis5zv4hdBLWPens--UF8hi3YqKHiWf3Rv-O'

    file_from = image_name
    file_to = '/Test/'+image_name

    dbx = dropbox.Dropbox(access_token)

    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("FILE HAS BEEN SUCCEFULLY UPLOADED")

def main():
    while True:
        if((time.time()-start_time)>=3):
            img = take_Snapshot()
            upload_files(img)


take_Snapshot()