import math
chang1 = 2.150579
kuan1 = 0.930413
chang2 = 0.814464
kuan2 = 1.521644
chang3 = 0.292397
kuan3 = 0.276281
height1 = 1.12843
height2 = 0.601022
height3 = 0.231042
num_floors = 6
num_windows = 185


def yuan(r):
    return r*r*math.pi


max_width = kuan2
max_length = chang1 + chang2
window_width = 0.101021
window_height = 0.100211
factor = 1.87677 / window_height
ju1 = chang1 * kuan1
kon1 = chang2 * kuan2
ju2 = chang3 * kuan3

lou1 = chang1 * kuan1 * height1

lou2 = chang2 * kuan2 * height2

lou3 = chang3 * kuan3 * height3

volume = lou1 + lou2 + lou3

real_volume = volume * factor * factor * factor
print("num_floors:", num_floors)
print("num_windows:", num_windows)
print("max_width:", max_width * factor)
print("max_length:", max_length * factor)
print("max_height:", (height1 + height3) * factor)
print("volume:", real_volume)
print("window height:", window_height * factor)
print("window width:", window_width * factor)
print("window square:", num_windows * window_height * window_width * factor * factor)
