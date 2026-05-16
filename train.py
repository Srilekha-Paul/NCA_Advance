# train.py

import torch
import torch.optim as optim
import torch.nn.functional as F
import numpy as np

from advanced_model import NeuralCA
from targets import make_target_tensor

# =====================================================
# CONFIG
# =====================================================
DEVICE = "cpu"
CHANNELS = 16
SIZE = 64
EPOCHS = 1000
STEPS_MIN = 32
STEPS_MAX = 64
LR = 1e-4

# =====================================================
# SEED GRID
# =====================================================
def make_seed(size=64, channels=16):
    x = torch.zeros(1, channels, size, size)
    x[:, 3:, size//2, size//2] = 1.0
    return x

# =====================================================
# TRAIN
# =====================================================
def train(target_name="heart"):

    model = NeuralCA(channels=CHANNELS).to(DEVICE)
    optimizer = optim.Adam(model.parameters(), lr=LR)

    target = make_target_tensor(target_name).to(DEVICE)

    pool = make_seed().repeat(8, 1, 1, 1)

    for epoch in range(EPOCHS):

        batch = pool[:4].clone()

        steps = np.random.randint(STEPS_MIN, STEPS_MAX)

        for _ in range(steps):
            batch = model(batch)

        loss = F.mse_loss(batch[:, :4], target.repeat(4,1,1,1))

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        pool[:4] = batch.detach()

        if epoch % 50 == 0:
            print(f"Epoch {epoch} | Loss: {loss.item():.5f}")

    torch.save(model.state_dict(), "saved/best_model.pth")
    print("✅ Model Saved")


if __name__ == "__main__":
    train("heart")










# # train.py

# import numpy as np
# import time

# from model import SimpleNCA
# from targets import get_target
# from utils import create_seed, calc_similarity


# # =========================================================
# # CONFIG
# # =========================================================
# TARGET_NAME = "Heart"     # Heart / Gecko / Emoji
# EPOCHS = 300
# STEPS_PER_EPOCH = 25


# # =========================================================
# # TRAIN LOOP
# # =========================================================
# def train():
#     print("=" * 60)
#     print("🧬 Adaptive Neural Cellular Automata Training Started")
#     print("=" * 60)

#     model = SimpleNCA()
#     target = get_target(TARGET_NAME)

#     best_score = 0

#     for epoch in range(1, EPOCHS + 1):

#         # Start from seed
#         grid = create_seed()

#         # Grow organism
#         for _ in range(STEPS_PER_EPOCH):
#             grid = model.update(grid, target)

#         # Measure similarity
#         score = calc_similarity(grid, target)

#         # Track best
#         if score > best_score:
#             best_score = score

#         # Print progress
#         if epoch % 10 == 0 or epoch == 1:
#             print(
#                 f"Epoch {epoch:03d}/{EPOCHS} | "
#                 f"Accuracy: {score:.2f}% | "
#                 f"Best: {best_score:.2f}%"
#             )

#         time.sleep(0.02)

#     print("\n✅ Training Completed")
#     print(f"🏆 Best Accuracy: {best_score:.2f}%")
#     print("=" * 60)


# # =========================================================
# # MAIN
# # =========================================================
# if __name__ == "__main__":
#     train()

















# import torch
# import numpy as np
# from model import NCA
# from utils import seed_grid

# device = "cuda" if torch.cuda.is_available() else "cpu"

# model = NCA().to(device)
# optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

# for epoch in range(500):

#     x = seed_grid().to(device)

#     for i in range(50):
#         x = model(x)

#     loss = (x**2).mean()

#     optimizer.zero_grad()
#     loss.backward()
#     optimizer.step()

#     if epoch % 50 == 0:
#         print("Epoch:", epoch, "Loss:", loss.item())

# torch.save(model.state_dict(),"saved/nca.pth")
# print("Model Saved")