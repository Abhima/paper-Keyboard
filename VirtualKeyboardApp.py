import cv2
#importing keys values
import keyCode as kC
import time
import win32api

# Reading template image
template = cv2.imread("images/arrowTmpl.jpg", 0)
img_w, img_h = template.shape[::-1]

# creating variable to capture video
cap = cv2.VideoCapture(0)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH) # width of video captured by the webcam
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) #height of the video captured by the webcam

def main():

    while (True):

        # capturing live video
        ret, frame = cap.read()
        # flipping video upside down
        frame = cv2.flip(frame, -1)
        # resizing the dimensions
        resized = cv2.resize(frame, (640, 480), interpolation=cv2.INTER_LINEAR)

        # Creating rectangular sub window
        cv2.rectangle(resized, (640, 480), (0, 0), (0, 255, 0), 0)
        # Croping the captured video
        crop_frame = frame[5:480, 5:640]

        # Converting video to Grayscale
        grayVideo = cv2.cvtColor(crop_frame, cv2.COLOR_BGR2GRAY)
        # Applying gaussian blur
        blurVideo = cv2.GaussianBlur(grayVideo, (11, 11), 0)
        cv2.imshow("Blur Video", blurVideo) # Displaying blur video
        cv2.imshow("Template", template) # Displaying template image

        # Comparing video with template
        res = cv2.matchTemplate(blurVideo, template, cv2.TM_CCOEFF_NORMED)
        #res = cv2.matchTemplate(binaryVideo, template, cv2.TM_CCORR_NORMED)

        # Storing coordinates of template matching area
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        top_left = max_loc
        xAxis = int(round(top_left[0] + (img_w / 2)))
        yAxis = int(round(top_left[1] + (img_h / 2)))

        #print("Template match rate(100%):",max_val * 100)

        # Displaying pixel area and percentage of template matching on the screen
        cv2.putText(resized, "X-Axix: " + str(xAxis) + " and " + "Y-Axis: " + str(yAxis), (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, 2)
        cv2.putText(resized, "Template match rate(100%):" + str(int(max_val*100))+ "%", (10, 450),
                    cv2.QT_FONT_NORMAL, 1, (0,255,0), 1)


        if max_val > 0.5:
            # duration of key pressing i.e 1 second
            holdingTime = 1

            bottom_right = (top_left[0] + img_w, top_left[1] + img_h)
            # Drawing pointer and rectangle on the template matched pixel area
            cv2.rectangle(resized, top_left, bottom_right, (0, 0, 255), 4)
            cv2.circle(resized, (xAxis, yAxis), 3, (255, 0, 0), 4)

            # Implementing condition to divide captured video into dimension of respective key
            # And triggering typing key event

            ###*** First row starts ***###
            if xAxis > 0 and xAxis <= 64 and yAxis <= 120:
                win32api.keybd_event(kC.VK_CODE['q'], 0, 0, 0)
                time.sleep(holdingTime)

            elif xAxis > 65 and xAxis <= 128 and yAxis <= 120:
                win32api.keybd_event(kC.VK_CODE['w'], 0, 0, 0)
                time.sleep(holdingTime)

            elif xAxis > 129 and xAxis <= 192 and yAxis <= 120:
                win32api.keybd_event(kC.VK_CODE['e'], 0, 0, 0)
                time.sleep(holdingTime)

            elif xAxis > 193 and xAxis <= 256 and yAxis <= 120:
                win32api.keybd_event(kC.VK_CODE['r'], 0, 0, 0)
                time.sleep(holdingTime)

            elif xAxis > 257 and xAxis <= 320 and yAxis <= 120:
                win32api.keybd_event(kC.VK_CODE['t'], 0, 0, 0)
                time.sleep(holdingTime)

            elif xAxis > 321 and xAxis <= 384 and yAxis <= 120:
                win32api.keybd_event(kC.VK_CODE['y'], 0, 0, 0)
                time.sleep(holdingTime)

            elif xAxis > 385 and xAxis <= 448 and yAxis <= 120:
                win32api.keybd_event(kC.VK_CODE['u'], 0, 0, 0)
                time.sleep(holdingTime)

            elif xAxis > 449 and xAxis <= 512 and yAxis <= 120:
                win32api.keybd_event(kC.VK_CODE['i'], 0, 0, 0)
                time.sleep(holdingTime)

            elif xAxis > 513 and xAxis <= 576 and yAxis <= 120:
                win32api.keybd_event(kC.VK_CODE['o'], 0, 0, 0)
                time.sleep(holdingTime)

            elif xAxis > 577 and xAxis <= 640 and yAxis <= 120:
                win32api.keybd_event(kC.VK_CODE['p'], 0, 0, 0)
                time.sleep(holdingTime)

            ###*** Second row starts ***###
            elif xAxis > 0 and xAxis <= 64 and yAxis >= 121 and yAxis <= 240:
                win32api.keybd_event(kC.VK_CODE['a'], 0, 0, 0)
                time.sleep(holdingTime)

            elif xAxis > 65 and xAxis <= 128 and yAxis >= 121 and yAxis <= 240:
                win32api.keybd_event(kC.VK_CODE['s'], 0, 0, 0)
                time.sleep(holdingTime)

            elif xAxis > 129 and xAxis <= 192 and yAxis >= 121 and yAxis <= 240:
                win32api.keybd_event(kC.VK_CODE['d'], 0, 0, 0)
                time.sleep(holdingTime)

            elif xAxis > 193 and xAxis <= 256 and yAxis >= 121 and yAxis <= 240:
                win32api.keybd_event(kC.VK_CODE['f'], 0, 0, 0)
                time.sleep(holdingTime)

            elif xAxis > 257 and xAxis <= 320 and yAxis >= 121 and yAxis <= 240:
                win32api.keybd_event(kC.VK_CODE['g'], 0, 0, 0)
                time.sleep(holdingTime)

            elif xAxis > 321 and xAxis <= 384 and yAxis >= 121 and yAxis <= 240:
                win32api.keybd_event(kC.VK_CODE['h'], 0, 0, 0)
                time.sleep(holdingTime)

            elif xAxis > 385 and xAxis <= 448 and yAxis >= 121 and yAxis <= 240:
                win32api.keybd_event(kC.VK_CODE['j'], 0, 0, 0)
                time.sleep(holdingTime)

            elif xAxis > 449 and xAxis <= 512 and yAxis >= 121 and yAxis <= 240:
                win32api.keybd_event(kC.VK_CODE['k'], 0, 0, 0)
                time.sleep(holdingTime)

            elif xAxis > 513 and xAxis <= 576 and yAxis >= 121 and yAxis <= 240:
                win32api.keybd_event(kC.VK_CODE['l'], 0, 0, 0)
                time.sleep(holdingTime)

            elif xAxis > 577 and xAxis <= 640 and yAxis >= 121 and yAxis <= 240:
                win32api.keybd_event(kC.VK_CODE['enter'], 0, 0, 0)
                time.sleep(holdingTime)

            ###*** Third row starts ***###
            elif xAxis > 0 and xAxis <= 64 and yAxis >= 241 and yAxis <= 360:
                win32api.keybd_event(kC.VK_CODE['z'], 0, 0, 0)
                time.sleep(holdingTime)

            elif xAxis > 65 and xAxis <= 128 and yAxis >= 241 and yAxis <= 360:
                win32api.keybd_event(kC.VK_CODE['x'], 0, 0, 0)
                time.sleep(holdingTime)

            elif xAxis > 129 and xAxis <= 192 and yAxis >= 241 and yAxis <= 360:
                win32api.keybd_event(kC.VK_CODE['c'], 0, 0, 0)
                time.sleep(holdingTime)

            elif xAxis > 193 and xAxis <= 256 and yAxis >= 241 and yAxis <= 360:
                win32api.keybd_event(kC.VK_CODE['v'], 0, 0, 0)
                time.sleep(holdingTime)

            elif xAxis > 257 and xAxis <= 320 and yAxis >= 241 and yAxis <= 360:
                win32api.keybd_event(kC.VK_CODE['b'], 0, 0, 0)
                time.sleep(holdingTime)

            elif xAxis > 321 and xAxis <= 384 and yAxis >= 241 and yAxis <= 360:
                win32api.keybd_event(kC.VK_CODE['n'], 0, 0, 0)
                time.sleep(holdingTime)

            elif xAxis > 385 and xAxis <= 448 and yAxis >= 241 and yAxis <= 360:
                win32api.keybd_event(kC.VK_CODE['m'], 0, 0, 0)
                time.sleep(holdingTime)

            elif xAxis > 193 and xAxis <= 448 and yAxis >= 361 and yAxis <= 480:
                win32api.keybd_event(kC.VK_CODE['spacebar'], 0, 0, 0)
                time.sleep(holdingTime)

            else:
                print('')
        cv2.imshow("grayVideo", grayVideo) # Displaying video in grayscale
        cv2.imshow("Resized Video", resized) # Displaying Final video
        if cv2.waitKey(1) & 0xFF == ord("q"): # Defining letter "q" to close program when pressed
            break

    cap.release()
    cv2.destroyAllWindows()
main()
