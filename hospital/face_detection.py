from django import template
register = template.Library()


import os
import cv2
import face_recognition


def image_capture():
    folder_name = "face_images"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    existing_face_images = [f for f in os.listdir(folder_name) if os.path.isfile(os.path.join(folder_name, f))]
    num_existing_face_images = len(existing_face_images)

    cv2.namedWindow("Collecting Your Face")
    cap = cv2.VideoCapture(0)

    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    num_frames = 50

    face_images = []

    for i in range(num_frames):
        # Read a frame from the video stream
        ret, frame = cap.read()

        # Convert the frame from BGR to RGB
        rgb_frame = frame[:, :, ::-1]

        # Detect faces in the RGB image
        face_locations = face_recognition.face_locations(rgb_frame)

        # Loop through the faces
        for (top, right, bottom, left) in face_locations:
            # Draw a rectangle around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

            # Crop the face region from the RGB image
            face_image = rgb_frame[top:bottom, left:right]

            # Resize the face image to a fixed size (e.g., 100x100)
            face_image = cv2.resize(face_image, (100, 100))

            # Generate a unique filename for the face image
            filename = "face_{}.jpg".format(num_existing_face_images + len(face_images))

            # Save the face image to the folder
            filepath = os.path.join(folder_name, filename)
            cv2.imwrite(filepath, face_image)

            # Store the filename in the list
            face_images.append(filename)

        # Display the frame in the window
        cv2.imshow("Face Data Collection", frame)

        # Wait for a key press to move to the next frame
        if cv2.waitKey(1) == ord('q'):
            break

    # Release the video capture object and close the window
    cap.release()
    cv2.destroyAllWindows()

    # Print the number of face images collected
    print("Number of face images collected: ", len(face_images))

    # Print the filenames of the collected face images
    print("Filenames of the collected face images:")
    for filename in face_images:
        print(filename)


