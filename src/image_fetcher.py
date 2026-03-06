import requests
import os


def download_image(destination):

    folder = "assets/destinations"
    os.makedirs(folder, exist_ok=True)

    filename = destination.lower().replace(" ", "_") + ".jpg"
    filepath = os.path.join(folder, filename)

    if os.path.exists(filepath):
        return filepath

    search = destination.replace(" ", "_")

    url = f"https://commons.wikimedia.org/wiki/Special:FilePath/{search}.jpg"

    try:
        img = requests.get(url, timeout=10)

        if img.status_code == 200 and len(img.content) > 1000:

            with open(filepath, "wb") as f:
                f.write(img.content)

            return filepath

    except:
        pass

    return None