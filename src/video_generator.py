import os
import cv2

IMAGE_FOLDER = "assets/destinations"
VIDEO_OUTPUT = "travel_video.mp4"


def generate_travel_video(itinerary):

    images = []

    for day in itinerary:

        destination = day["destination"]

        # convert name to file format
        filename = destination.lower().replace(" ", "_") + ".jpg"

        path = os.path.join(IMAGE_FOLDER, filename)

        if os.path.exists(path):

            img = cv2.imread(path)

            img = cv2.resize(img, (1280, 720))

            images.append(img)

    if len(images) == 0:
        return None

    video = cv2.VideoWriter(
        VIDEO_OUTPUT,
        cv2.VideoWriter_fourcc(*"mp4v"),
        1,
        (1280, 720)
    )

    for img in images:

        for _ in range(2):
            video.write(img)

    video.release()

    return VIDEO_OUTPUT