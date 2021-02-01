import cv2 as cv
import random
import os


# def load_data(path):
#     data = []
#     count = 0
#     for dirs in os.listdir(path):
#         sign_list = os.listdir(path + "/{}".format(dirs))
#         for cat in sign_list:
#             files = path + "/{}/{}".format(dirs, cat)
#             image = cv.imread(files)
#             image = cv.resize(image, (1280, 720))
#             cv.imwrite("gambar/{}.jpg".format(count), image)
#             print("[INFO] {}.jpg saved ..".format(count))
#             count += 1
#     print("[INFO] Done saving ..")

def load_data(path):
    data = []
    for item in os.listdir(path):
        files = path + "/{}".format(item)
        image = cv.imread(files)
        # image = cv.resize(image, (1280, 720))
        data.append(image)
    random.shuffle(data)
    return data


def save_data(path):
    images = load_data(path)
    count = 640
    for image in images:
        cv.imwrite("shuffle/test/{}.jpg".format(count), image)
        print("[INFO] {}.jpg saved ..".format(count))
        count += 1
    print("[INFO] Done saving ..")


save_data("images/test")
