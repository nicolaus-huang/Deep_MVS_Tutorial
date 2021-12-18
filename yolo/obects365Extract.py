import os
import argparse



import json
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import cv2
import shutil
import os
import subprocess
import argparse
import glob
from tqdm import tqdm
import time


# cellphone:79 key:266 handbag:13 laptop:77
# classes_names = {79: "cellphone", 266: "key", 13: "handbag", 77: "laptop"}

def save_annotations( anno_file_path, imgs_file_path,output_dir,objects_2_my_classes):
    '''
    :param classes_names: #如果该种类比如1 3被选取那么{1:person,3:chair}
    :param anno_file_path:  # D:\jsonProcess\input\val.json
    :param imgs_file_path:  # #D:\jsonProcess\input\image
    :param output_dir:  /output
    :return:
    '''
    # open json file(val.json or train.json)
    with open(anno_file_path, 'r') as f:
        data = json.load(f)
        # 900w+
        print("anno count:", len(data["annotations"]))
        print("image count:", len(data["images"]))
        img_map = {}    #编号到宽,高,名的映射354609->{}
        img_2_anno = {} #编号到类别,bbox等的映射354609->[{},{}]
        name_2_id={}    #名称到编号映射obj365_val_000000354609.jpg->354609
        images_in_dir = set(os.listdir(imgs_file_path)) #查找时间复杂度O(1)
        for i in data["images"]:
            if i["file_name"] in images_in_dir:
                img_map[i["id"]] = i    # {354609:{'id': 354609, 'height': 512, 'file_name': 'obj365_val_000000354609.jpg', 'width': 683},567733:{'image_id': 567733, 'area': 238074.4957648346, 'category_id': 1, 'id': 4, 'iscrowd': 0, 'bbox': [71.744506816, 60.36883545599999, 568.121826176, 419.055358896]}}
                img_2_anno[i["id"]] = []    #{354609:[],567733:[]}一口气弄完了
                name_2_id[i["file_name"]]=i["id"]
        for anno in data["annotations"]:#一口气弄完了
            if anno["image_id"] in img_map.keys() and anno["category_id"] in objects_2_my_classes.keys(): #如果文件夹里有该照片且该照片有需要的类
                anno["category_id"]=objects_2_my_classes[anno["category_id"]]   #换到我自己的类
                img_2_anno[anno["image_id"]].append(anno)   #{354609:[{'image_id': 354609, 'area': 13467.531777104436, 'category_id': 3, 'id': 1, 'iscrowd': 0, 'bbox': [289.74798586220004, 215.75781248, 127.72149654100002, 105.44451906559996]},{'image_id': 354609, 'area': 54688.424399724776, 'category_id': 3, 'id': 2, 'iscrowd': 0, 'bbox': [339.4999999909, 279.6185912832, 258.41333009830004, 211.6315918336]}]}
        # del data
        for _, id in enumerate(img_2_anno):#开始一张张处理图片
            annos = img_2_anno[id]  #354609对应的[{'image_id': 354609, 'area': 13467.531777104436, 'category_id': 3, 'id': 1, 'iscrowd': 0, 'bbox': [289.74798586220004, 215.75781248, 127.72149654100002, 105.44451906559996]},{'image_id': 354609, 'area': 54688.424399724776, 'category_id': 3, 'id': 2, 'iscrowd': 0, 'bbox': [339.4999999909, 279.6185912832, 258.41333009830004, 211.6315918336]}]
            if len(annos) > 0:  #有所要识别的对象
                img = img_map[id]
                img_width = img["width"]
                img_height = img["height"]
                objs = []
                for anno in annos:
                    bbox = anno["bbox"]
                    x = min(max(bbox[0]+bbox[2]/2,0)/img_width,1)   #大于0小于1(有标记有误差的的)
                    y = min(max(bbox[1]+bbox[3]/2,0)/img_height,1)
                    w =min(max(bbox[2]/img_width,0),1)
                    h=min(max(bbox[3]/img_height,0),1)
                    my_class_id = anno["category_id"]
                    obj = [my_class_id, x, y, w, h]
                    objs.append(obj)
                shutil.copy(os.path.join(imgs_file_path,img_map[id]['file_name']),os.path.join(output_dir,"images",'train'))    #复制图片到文件夹
                write_txt(output_dir,img_map[id]['file_name'],objs)
    print(" conver is done ")


def write_txt(output_dir, img_name,objs):
    img_name = img_name[:-4]
    list_name = os.path.join(output_dir,"labels",'train',img_name)+".txt"
    with open(list_name, 'w', encoding='utf-8') as list_fs:
        for line in objs:        # list_f.write(lines)
            line = str(int(line[0]))+" "+str(line[1])[:6]+" "+str(line[2])[:6]+" "+str(line[3])[:6]+" "+str(line[4])[:6]+"\n"
            list_fs.write(line)
        list_fs.close()

def main_object365(classes, input_dir, output_dir):
    # use ids match classes
    '''

    :param classes: [1,2,3]
    :param input_dir: objects365
    :param output_dir: 输出

    :return:
    '''
    classes_names = {}
    object_2_my_classes={}      #由objects365对应类别序号到我的序号1,4,8->0,1,2
    for i in range(len(classes)):
        object_2_my_classes[classes[i]]=i
    anno_file_path ="/public/home/huanggroup6/train.json" # D:\jsonProcess\input\val.json
    imgs_file_path = "/public/home/huanggroup6/train_part1/train"
    save_annotations(anno_file_path, imgs_file_path,output_dir,object_2_my_classes)

def main():
    input_dir = "input"
    classes = [9,14,33,35,59,103,145]  # object365_dict.txt里面的类
    output_dir = "output"
    main_object365(classes, input_dir, output_dir)


if __name__ == '__main__':
    main()
