import numpy as np
import matplotlib.pyplot as plt


def tensor_to_image(x):
    x = x.detach().cpu().numpy()[0, 0]
    x = np.clip(x, 0, 1)
    return x


def plot_tensor(img, title="NCA"):
    fig, ax = plt.subplots(figsize=(10, 7))

    ax.imshow(img, cmap="magma")

    ax.set_xticks([])
    ax.set_yticks([])

    ax.set_title(
        title,
        fontsize=24,
        fontweight="bold",
        color="white"
    )

    fig.patch.set_facecolor('#0b1120')
    ax.set_facecolor('#0b1120')

    return fig



# # utils.py

# import torch
# import numpy as np
# import matplotlib.pyplot as plt


# # =====================================================
# # CONVERT MODEL OUTPUT TO IMAGE
# # =====================================================
# def tensor_to_image(x):
#     """
#     Input:
#         Tensor shape = [1, C, H, W]

#     Output:
#         numpy image (H,W)
#     """

#     img = x[0, 3].detach().cpu().numpy()

#     img = np.clip(img, 0, 1)

#     return img


# # =====================================================
# # SHOW IMAGE
# # =====================================================
# def plot_tensor(x, title="NCA Output"):

#     img = tensor_to_image(x)

#     fig, ax = plt.subplots(figsize=(8, 8))

#     fig.patch.set_facecolor("#0a0d14")
#     ax.set_facecolor("#0a0d14")

#     ax.imshow(img, cmap="viridis", vmin=0, vmax=1)

#     ax.set_title(
#         title,
#         color="white",
#         fontsize=16,
#         fontweight="bold"
#     )

#     ax.axis("off")

#     return fig


# # =====================================================
# # DAMAGE ORGANISM
# # =====================================================
# def damage_tensor(x, mode="center"):

#     y = x.clone()

#     _, _, h, w = y.shape

#     if mode == "center":
#         y[:, :, h//3:2*h//3, w//3:2*w//3] = 0

#     elif mode == "left":
#         y[:, :, :, :w//2] = 0

#     elif mode == "right":
#         y[:, :, :, w//2:] = 0

#     elif mode == "random":
#         mask = torch.rand_like(y[:, :1]) > 0.7
#         y = y * (~mask)

#     return y


# # =====================================================
# # MAKE SEED
# # =====================================================
# def make_seed(size=64, channels=16):

#     x = torch.zeros(1, channels, size, size)

#     x[:, 3:, size//2, size//2] = 1.0

#     return x


# # =====================================================
# # SIMILARITY
# # =====================================================
# def calc_accuracy(pred, target):

#     p = pred[:, 3].detach().cpu().numpy() > 0.5
#     t = target[:, 3].detach().cpu().numpy() > 0.5

#     score = (p == t).mean() * 100

#     return score






























# # utils.py

# import numpy as np
# import matplotlib.pyplot as plt


# # =========================================================
# # DAMAGE GRID
# # =========================================================
# def damage_grid(grid, mode="center"):
#     """
#     Remove part of organism for self-healing tests
#     """

#     g = grid.copy()
#     h, w = g.shape

#     if mode == "center":
#         g[h//3:2*h//3, w//3:2*w//3] = 0

#     elif mode == "left":
#         g[:, :w//2] = 0

#     elif mode == "right":
#         g[:, w//2:] = 0

#     elif mode == "random":
#         mask = np.random.rand(h, w) > 0.7
#         g[mask] = 0

#     return g


# # =========================================================
# # RENDER GRID
# # =========================================================
# def render_grid(grid, title="NCA Output"):
#     """
#     Display organism grid professionally
#     """

#     fig, ax = plt.subplots(figsize=(8, 8))

#     fig.patch.set_facecolor("#0a0d14")
#     ax.set_facecolor("#0a0d14")

#     img = ax.imshow(
#         grid,
#         cmap="viridis",
#         vmin=0,
#         vmax=1,
#         interpolation="nearest"
#     )

#     ax.set_title(
#         title,
#         color="white",
#         fontsize=18,
#         fontweight="bold",
#         pad=15
#     )

#     ax.axis("off")

#     return fig


# # =========================================================
# # CALCULATE ACCURACY
# # =========================================================
# def calc_similarity(grid, target):
#     """
#     Percentage similarity between current state and target
#     """

#     binary_grid = (grid > 0.5).astype(np.float32)
#     binary_target = (target > 0.5).astype(np.float32)

#     match = np.mean(binary_grid == binary_target)

#     return match * 100


# # =========================================================
# # LIVE CELL COUNT
# # =========================================================
# def count_live_cells(grid):
#     return int((grid > 0.2).sum())


# # =========================================================
# # RESET GRID
# # =========================================================
# def create_seed(size=64):
#     """
#     Single seed cell in center
#     """

#     grid = np.zeros((size, size), dtype=np.float32)
#     grid[size//2, size//2] = 1.0

#     return grid


# # =========================================================
# # NOISE GRID
# # =========================================================
# def add_noise(grid, amount=0.05):
#     """
#     Add small random mutations
#     """

#     noise = np.random.rand(*grid.shape) * amount

#     g = grid + noise

#     return np.clip(g, 0, 1)











# import torch

# def seed_grid(size=64):
#     x = torch.zeros(1,16,size,size)
#     x[:,:,size//2,size//2] = 1.0
#     return x