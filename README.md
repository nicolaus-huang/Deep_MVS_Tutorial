# Deep_MVS_Tutorial
 A simple tutorial for beginners to learning based MVS. We were doing some homework towards reconstruction our campus, and here we share some detail, further detail about our work can be found in [Bilibili]( ) and [Youtube]().

First of all, let's get some basic knowledge of learning based MVS method. MVS ( Muti-View Stereo ) is a submission of computer version, which aims to turn images toward an object to an object ( in 3D format ). 

The methods now divides into two part: traditional MVS method and learning based MVS method, you can learn about traditional MVS methods by read [Multi-View Stereo: A Tutorial (PDF) ](https://www.nowpublishers.com/article/DownloadSummary/CGV-052) , and you can find a list of recent learning based MVS method in [Awesome-Learning-MVS](https://github.com/XYZ-qiyh/Awesome-Learning-MVS) .

To turn some images into a point cloud, you need to know the where the cameras are and some information of the cameras, the progress is called Sfm ( Structure-from-Motion ) , you need to do this in almost all MVS method, but it's not important because mostly the task use a traditional method.

**The learning task is simple:** After getting the information of your cameras, the networks shows up, feed the information and images to them, and that comes out the disparity map, which refer to the truly depth of each pixel in the image.

| Special File formats | Meaning            |
| -------------------- | ------------------ |
| .pfm                 | disparity map file |
| .ply                 | point cloud file   |

Different to Mono-Depth Estimating task, the methods in MVS project focus on the relationship between images, by different understanding of corresponding feature in images, people propose many tricks to generate the disparity map. After got the disparity map you should find some way to do the fusion task, which aims to turn the disparity map to point cloud, this step varies a lot between different methods, but some of them require a repo [fusibile](https://github.com/kysucix/fusibile) .

| Useful Software                               | Most Usages                                   |
| --------------------------------------------- | --------------------------------------------- |
| [COLMAP](https://colmap.github.io/)           | Sfm                                           |
| [MeshLab](https://www.meshlab.net/)           | view the .ply file                            |
| [CloudCompare](https://www.danielgm.net/cc/)  | edit the .ply file (open **very** large .ply) |
| [cvkit](https://github.com/roboception/cvkit) | view .pfm file                                |

### PatchmatchNet

PatchmatchNet is the only method that we made some changes to the code and it's easy to understand the pipeline, we would like to share some detail about this network. Patchmatch is a traditional method, you can learn more about it by view [paper](https://gfx.cs.princeton.edu/pubs/Barnes_2009_PAR/patchmatch.pdf) and [Youtube](https://www.youtube.com/watch?v=m-kGXlomOxY&t=40s). PatchmatchNet made some changes to it and propose a deep learning way, details can be found in [paper](https://openaccess.thecvf.com/content/CVPR2021/papers/Wang_PatchmatchNet_Learned_Multi-View_Patchmatch_Stereo_CVPR_2021_paper.pdf) and [Github](https://github.com/FangjinhuaWang/PatchmatchNet), it requires the result from Sfm, which means the .bin files under the sparse folder if you are using COLMAP.

The preprocess and the fusion part goes too slow under bigger dataset, so we use [mutiprocessing](https://pypi.org/project/multiprocessing/) to parallelize them. Details can be found in our code, and we will offer the docker image for a quick start.

