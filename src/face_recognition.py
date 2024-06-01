import cv2 as cv
import face_recognition as face

cap = cv.VideoCapture(0)

known_image = face.load_image_file('img/meeee.jpg')
known_encodings = face.face_encodings(known_image)[0]
known_name = 'Sensei'

known_names = [known_name]

while True:
    ret, frame = cap.read()
    locations = face.face_locations(frame)
    encodings = face.face_encodings(frame, locations)

    for (top, right, bottom, left), encoding in zip(locations, encodings):
        matches = face.compare_faces([known_encodings], encoding)
        name = 'Unknown!'

        if True in matches:
            match_index = matches.index(True)
            name = known_names[match_index]

        cv.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv.putText(frame, name, (left, top - 10), cv.FONT_HERSHEY_SIMPLEX, 1, (36, 255, 12), 2)
    cv.imshow('Face Detection', frame)

    if cv.waitKey(1) == ord('Q'):
        break

cap.release()
cv.destroyAllWindows()
