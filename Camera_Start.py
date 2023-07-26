import cv2

def list_all_avaliable_cams():
    max_num_cams = 10
    ava_source_index = []
    for i in range(max_num_cams):
        cap = cv2.VideoCapture(i)
        if cap is None or not cap.isOpened():
            print("Total number of available Webcam = {:d}".format(i))
            break
        else:
            print("Available cam at source: {}".format(i))
            ava_source_index.append(i)
    return ava_source_index

def start_capture(i):
    # Create a VideoCapture object to access the webcam (0 refers to the default webcam, change to 1 if you have an external webcam).
    cap = cv2.VideoCapture(i)

    if not cap.isOpened():
        print("Error: Could not access the webcam.")
        return

    while True:
        # Capture a frame from the webcam
        ret, frame = cap.read()

        if not ret:
            print("Error: Couldn't read a frame.")
            break

        # Display the frame in a window
        cv2.imshow("Webcam", frame)

        # Check for 'q' key press, and exit the loop if pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the VideoCapture and destroy any OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

def main():
    camlist = list_all_avaliable_cams()
    print("All available source cam index list: {}".format(camlist))

    print("Please select camera source for start: ")
    usr_sel_input = input()
    for i in camlist:
        if usr_sel_input == str(i):
            start_capture(i)
        else:
            print("Please select a valid camera!")

if __name__ == "__main__":
    main()
