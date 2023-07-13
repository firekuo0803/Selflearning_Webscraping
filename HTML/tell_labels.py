import os
import cv2
import shutil

dir_img = 'd_images'
dir_lab = 'd_labels'

path_img ='dragon_ball/golf'
path_lab ='dragon_ball/labels'

img_list = os.listdir(path_img)
lab_list = os.listdir(path_lab)

img_names =[]
label_names=[]
count_img = 0
count_lab = 0

if not os.path.isdir(dir_img):
    os.mkdir(dir_img)
if not os.path.isdir(dir_lab):
    os.mkdir(dir_lab)

for nimg in img_list:
    img_names.append(os.path.splitext(nimg)[0])
for nlab in lab_list:
    label_names.append(os.path.splitext(nlab)[0])

for img in img_names:

    for i in range(len(label_names)):
        lab = label_names[i]
        if img == lab:
            try:
                img2 = cv2.imread(f'D:/Desktop/HTML/{path_img}/{img_list[count_img]}')
                cv2.imwrite(f'D:/Desktop/HTML/{dir_img}/{img_list[count_img]}', img2)
                src = f'D:/Desktop/HTML/{path_lab}/{lab_list[i]}'
                dst = f'D:/Desktop/HTML/{dir_lab}/{lab_list[i]}'
                x = open(dst, 'a')
                x.write("")
                x.close()
                dst2 = rf'D:/Desktop/HTML/{dir_lab}/{lab_list[i]}'
                shutil.copyfile(src, dst2)
            except:
                pass
    count_img+=1