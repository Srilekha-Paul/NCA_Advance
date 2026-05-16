# targets.py

import torch
import numpy as np

SIZE = 64


# =====================================================
# HEART TARGET
# =====================================================
def heart_array():
    x = np.linspace(-2, 2, SIZE)
    y = np.linspace(-2, 2, SIZE)

    X, Y = np.meshgrid(x, y)

    Z = (X**2 + Y**2 - 1)**3 - X**2 * Y**3

    img = (Z <= 0).astype(np.float32)

    return img


# =====================================================
# GECKO TARGET
# =====================================================
def gecko_array():
    img = np.zeros((SIZE, SIZE), dtype=np.float32)

    # Body
    img[28:36, 18:46] = 1.0

    # Head
    img[26:38, 44:54] = 1.0

    # Tail
    img[30:34, 8:20] = 1.0

    # Legs
    img[18:28, 22:26] = 1.0
    img[36:46, 22:26] = 1.0
    img[18:28, 38:42] = 1.0
    img[36:46, 38:42] = 1.0

    return img


# =====================================================
# EMOJI TARGET
# =====================================================
def emoji_array():
    img = np.zeros((SIZE, SIZE), dtype=np.float32)

    yy, xx = np.ogrid[:SIZE, :SIZE]

    face = (xx - 32)**2 + (yy - 32)**2 <= 22**2
    img[face] = 1.0

    # Eyes
    eye1 = (xx - 24)**2 + (yy - 25)**2 <= 2**2
    eye2 = (xx - 40)**2 + (yy - 25)**2 <= 2**2

    img[eye1] = 0.0
    img[eye2] = 0.0

    # Smile
    for x in range(22, 42):
        y = int(40 - 0.03 * (x - 32)**2)
        if 0 <= y < SIZE:
            img[y:y+2, x] = 0.0

    return img


# =====================================================
# TO TENSOR
# Output Shape = [1,4,64,64]
# =====================================================
def make_target_tensor(name="heart"):

    name = name.lower()

    if name == "heart":
        arr = heart_array()

    elif name == "gecko":
        arr = gecko_array()

    elif name == "emoji":
        arr = emoji_array()

    else:
        arr = heart_array()

    # RGBA channels
    rgba = np.zeros((4, SIZE, SIZE), dtype=np.float32)

    rgba[0] = arr
    rgba[1] = arr
    rgba[2] = arr
    rgba[3] = arr

    tensor = torch.tensor(rgba).unsqueeze(0)

    return tensor




























# # targets.py

# import numpy as np

# SIZE = 64


# # =========================================================
# # HEART TARGET
# # =========================================================
# def heart():
#     x = np.linspace(-2, 2, SIZE)
#     y = np.linspace(-2, 2, SIZE)

#     X, Y = np.meshgrid(x, y)

#     Z = (X**2 + Y**2 - 1)**3 - X**2 * Y**3

#     target = (Z <= 0).astype(np.float32)

#     return target


# # =========================================================
# # EMOJI TARGET
# # =========================================================
# def emoji():
#     grid = np.zeros((SIZE, SIZE), dtype=np.float32)

#     yy, xx = np.ogrid[:SIZE, :SIZE]

#     # Face circle
#     face = (xx - 32)**2 + (yy - 32)**2 <= 22**2
#     grid[face] = 1.0

#     # Eyes
#     eye1 = (xx - 24)**2 + (yy - 25)**2 <= 2**2
#     eye2 = (xx - 40)**2 + (yy - 25)**2 <= 2**2

#     grid[eye1] = 0.0
#     grid[eye2] = 0.0

#     # Smile
#     for x in range(22, 42):
#         y = int(40 - 0.03 * (x - 32)**2)
#         if 0 <= y < SIZE:
#             grid[y:y+2, x] = 0.0

#     return grid


# # =========================================================
# # GECKO TARGET
# # =========================================================
# def gecko():
#     grid = np.zeros((SIZE, SIZE), dtype=np.float32)

#     # Body
#     grid[28:36, 18:46] = 1.0

#     # Head
#     grid[26:38, 44:54] = 1.0

#     # Tail
#     grid[30:34, 8:20] = 1.0

#     # Legs
#     grid[18:28, 22:26] = 1.0
#     grid[36:46, 22:26] = 1.0

#     grid[18:28, 38:42] = 1.0
#     grid[36:46, 38:42] = 1.0

#     return grid


# # =========================================================
# # EMPTY TARGET
# # =========================================================
# def blank():
#     return np.zeros((SIZE, SIZE), dtype=np.float32)


# # =========================================================
# # ROUTER
# # =========================================================
# def get_target(name):
#     name = name.lower()

#     if name == "heart":
#         return heart()

#     elif name == "emoji":
#         return emoji()

#     elif name == "gecko":
#         return gecko()

#     else:
#         return blank()












# import numpy as np

# def heart(size=64):
#     img = np.zeros((size,size,4), dtype=np.float32)

#     for y in range(size):
#         for x in range(size):
#             X=(x-size/2)/(size/2)
#             Y=(y-size/2)/(size/2)

#             if (X**2 + Y**2 -0.3)**3 - X**2*Y**3 <0:
#                 img[y,x,:3]=[1,0,0]
#                 img[y,x,3]=1

#     return img