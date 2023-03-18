from django import template
register = template.Library()

import cv2
import face_recognition

def check_face():
    known_face_encodings = []
    known_face_names = []

    face1_image = face_recognition.load_image_file("MESSI.jpg")
    face1_encoding = face_recognition.face_encodings(face1_image)[0]
    known_face_encodings.append(face1_encoding)
    known_face_names.append("Messi")

    face2_image = face_recognition.load_image_file("Cristiano Ronaldo.webp")
    face2_encoding = face_recognition.face_encodings(face2_image)[0]
    known_face_encodings.append(face2_encoding)
    known_face_names.append("Ronaldo")

    face3_image = face_recognition.load_image_file("Aloysius.jpg")
    face3_encoding = face_recognition.face_encodings(face3_image)[0]
    known_face_encodings.append(face3_encoding)
    known_face_names.append("Aloysius")

    face4_image = face_recognition.load_image_file("lance.jpg")
    face4_encoding = face_recognition.face_encodings(face4_image)[0]
    known_face_encodings.append(face4_encoding)
    known_face_names.append("Lance")

    video_capture = cv2.VideoCapture(0)

    while True:
        ret, frame = video_capture.read(3000)

        rgb_frame = frame[:, :, ::-1]

        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

            if True in matches:
                match_index = matches.index(True)
                name = known_face_names[match_index]
            else:
                name = "Unknown"

            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

        cv2.imshow('Image', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

check_face()