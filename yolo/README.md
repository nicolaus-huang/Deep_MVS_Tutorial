论文参考:
You Only Look Once:
Unified, Real-Time Object Detection
Joseph Redmon∗
, Santosh Divvala∗†, Ross Girshick¶
, Ali Farhadi∗†
University of Washington∗
, Allen Institute for AI†
, Facebook AI Research

YOLO9000:
Better, Faster, Stronger
Joseph Redmon∗†, Ali Farhadi∗†
University of Washington∗
, Allen Institute for AI†

YOLOv3: An Incremental Improvement Joseph Redmon, Ali Farhadi

源码参考:https://github.com/ultralytics/yolov3

训练数据存放格式参考mydata文件

配置文件参考data/mydata.yaml文件

测试结构见输出结果文件

原理参考目标检测.pptx文件

建筑物外围物体提取自objects365数据集,提取方法见objects365Extract.py,可方便地从数据集中提取想要的数据

数据集(两万张图片训练了近100轮)(感谢郭亮教授和中科曙光提供服务器)
