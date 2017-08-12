import urllib.request
import cv2
import numpy as np
import os


def store_raw_images():
    neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n02708433'
    neg_image_urls = urllib.request.urlopen(neg_images_link).read().decode()
    pic_num = 13


    if not os.path.exists('neg'):
        print("since there is no folder, we create new folder.")
        os.makedirs('neg')


    for i in neg_image_urls.split('\n'):
        try:
            print(i)
            urllib.request.urlretrieve(i, "neg/" + str(pic_num) + ".jpg")
            img = cv2.imread("neg/" + str(pic_num) + ".jpg", cv2.IMREAD_GRAYSCALE)
            # should be larger than samples / pos pic (so we can place our image on it)
            resized_image = cv2.resize(img, (100, 100))
            cv2.imwrite("neg/" + str(pic_num) + ".jpg", resized_image)
            pic_num += 1

        except Exception as e:
            print(str(e))


def find_uglies():
    match = False

    for file_type in ['neg']:
        #比較するファイルを格納したフォルダのファイル数分回す
        for img in os.listdir(file_type):

            #比較対象の写真をuglyフォルダから取得して一つずつ比較する。
            for ugly in os.listdir('ugly'):
                print(ugly.title() + "  " + img.title())
                try:
                    current_image_path = str(file_type) + '/' + str(img)
                    ugly = cv2.imread('ugly/'+str(ugly))
                    question = cv2.imread(current_image_path)

                    if ugly.shape == question.shape and not(np.bitwise_xor(ugly,question).any()):
                        print('That is one ugly pic! Deleting!')
                        print(current_image_path)
                        os.remove(current_image_path)
                    # else:
                    #     #print('this pic is OK.')
                except Exception as e:
                    print(str(e))


find_uglies()
#store_raw_images()

