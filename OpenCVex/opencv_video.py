import cv2


class video_play():
    def __init__(self):
        #self.video_file = "sample.mp4"
        self.video_file = "out.mp4"

    def frame_capture(self):
        cap = cv2.VideoCapture(self.video_file)
        while not cap.isOpened():
            cap = cv2.VideoCapture(self.video_file)
            cv2.waitKey(1000)
            print "Wait for the header"

        count = 0
        while True:
            ret, frame = cap.read()
            if ret:
                frm = cv2.resize(frame, (640,480))
                cv2.imshow('frame', frm)
                if cv2.waitKey(10) == 97:
                    cap.release()
                    cv2.destroyWindow('frame')
                    break
                count +=1
            else:
                print "Video Ended"
                print "Count :", count
                break

        # cv2.waitKey()
        # cap.release()
        return frame


def run():
    vc = video_play()
    selected_frame = vc.frame_capture()
    cv2.imshow('out',selected_frame)
    cv2.waitKey()


if __name__ == "__main__":
    run()