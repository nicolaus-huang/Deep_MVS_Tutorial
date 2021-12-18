import math
r1 = 2.49/2
r2 = 2.15/2
r3 = 0.32/2
r4 = 0.263/2
r5 = 0.077/2
r6 = 0.691/2
chang1 = 0.926821
kuan1 = 0.540230
chang2 = 0.507058
kuan2 = 0.224489
chang3 = 0.829926
kuan3 = 0.106065
chang4 = 0.587294
kuan4 = 0.602596
chang_daa = 0.476477
kuan_daa = 1.015017
chang_da = 1.015017
kuan_da = 0.182756
height1 = 0.413597
height2 = 0.790418
num_floors = 12
num_windows = 730


def yuan(r):
    return r*r*math.pi


yuanhuan = yuan(r1)/2 - yuan(r2)/2
dayuan = yuan(r3)/2
zhongyuan = yuan(r4)/2
xiaoyuan = yuan(r5)/2
banyuan = yuan(r6)/2
max_width = 3.654645
max_length = 2.588481
window_width = 0.051671
window_height = 0.03725
factor = 1.91846/window_height
ju1 = chang1 * kuan1
kon1 = chang2 * kuan2
ju2 = chang3 * kuan3
ju3 = chang4 * kuan4

da_lou = chang_daa * kuan_daa
da_ju = chang_da * kuan_da

lou1 = ((ju1 + yuanhuan - kon1 + ju2 + ju3 + zhongyuan*3 + xiaoyuan *
        2 + dayuan*2)*2 + banyuan + da_ju + da_lou) * height1

lou2 = da_lou * height2

volume = lou1 + lou2

real_volume = volume * factor * factor * factor
print("num_floors:", num_floors)
print("num_windows:", num_windows)
print("max_width:", max_width * factor)
print("max_length:", max_length * factor)
print("max_height:", (height1 + height2) * factor)
print("volume:", real_volume)
print("window height:", window_height * factor)
print("window width:", window_width * factor)
print("window square:", num_windows * window_height * window_width * factor * factor)
