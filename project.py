import cv2
import vlc
import time

class MyMediaPlayer():
    def __init__(self):
        self.face_detector = cv2.CascadeClassifier("res/haarcascade_frontalface_default.xml")
        self.eye_detector = cv2.CascadeClassifier("res/haarcascade_eye.xml")
        self.cap = cv2.VideoCapture(0)

    def stream_webcam(self):
        while True:
            ret, frame = self.cap.read()
            if ret:
                frame =  cv2.flip(frame, 1)
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                face_results = self.face_detector.detectMultiScale(gray)
                
                for(x, y, w, h) in face_results:
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                    cropped_gray = gray[y:y+h, x:x+w]
                    eye_results = self.eye_detector.detectMultiScale(cropped_gray)
                    for(eye_x, eye_y, eye_w, eye_h) in eye_results:
                        cv2.rectangle(frame, (x+eye_x, y+eye_y), (x+eye_x+eye_w, y+eye_y+eye_h), (0, 0, 255), 2)

                cv2.imshow("temp_frame", frame)
                q = cv2.waitKey(1)
                if q == ord('q'):
                    break

        cv2.destroyAllWindows()
        self.cap.release()
        
    def check_word(self):
        word = input("Menu: '1.music' | '2.movie' | '3.book' :  ")
        if word in("music", "1"):
            self.play_music()
        elif word in("movie", "2"):
            self.play_video()
        elif word in("book", "3"):
            print("Clean Code, Author: Robert Cecil Martin")
        else:
            print("The inserted word isn't valid.")
        
    def play_music(self):
        music = vlc.MediaPlayer("res/8-2-3_music.mp3")
        music.play()
        time.sleep(5)
        
    def play_video(self):
        player = vlc.MediaPlayer("res/video.mp4")
        player.play()
        time.sleep(5)
        # while True:
        #     if player.get_state() == vlc.State.Ended:
        #         break


mp = MyMediaPlayer()

# mp.check_word()
mp.stream_webcam()