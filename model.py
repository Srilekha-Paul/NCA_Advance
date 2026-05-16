# model.py

import numpy as np

class SimpleNCA:
    """
    Simple Neural Cellular Automata Engine
    Local neighbor-based growth + decay dynamics
    """

    def __init__(self, fire_rate=0.5):
        self.fire_rate = fire_rate

        # Neighborhood kernel
        self.kernel = np.array(
            [
                [0.05, 0.20, 0.05],
                [0.20, 0.00, 0.20],
                [0.05, 0.20, 0.05]
            ],
            dtype=np.float32
        )

    def convolve(self, grid):
        """
        Manual convolution (no scipy required)
        """
        padded = np.pad(grid, 1, mode="constant")
        out = np.zeros_like(grid)

        for i in range(grid.shape[0]):
            for j in range(grid.shape[1]):
                region = padded[i:i+3, j:j+3]
                out[i, j] = np.sum(region * self.kernel)

        return out

    def stochastic_mask(self, shape):
        """
        Random fire mask like true NCA update rate
        """
        return (np.random.rand(*shape) < self.fire_rate).astype(np.float32)

    def update(self, grid, target):
        """
        One cellular automata update step
        """

        # Perception from neighbors
        neighbors = self.convolve(grid)

        # Growth towards target + neighbor intelligence
        growth = (0.65 * neighbors) + (0.35 * target)

        # Decay old state + add growth
        new_grid = (grid * 0.88) + (growth * 0.22)

        # Apply stochastic updates
        mask = self.stochastic_mask(grid.shape)
        grid = grid * (1 - mask) + new_grid * mask

        # Clamp values
        grid = np.clip(grid, 0.0, 1.0)

        return grid

    def multi_update(self, grid, target, steps=10):
        """
        Run multiple updates
        """
        for _ in range(steps):
            grid = self.update(grid, target)
        return grid





# import torch
# import torch.nn as nn

# class NCA(nn.Module):
#     def __init__(self):
#         super().__init__()

#         self.net = nn.Sequential(
#             nn.Conv2d(16, 64, 1),
#             nn.ReLU(),
#             nn.Conv2d(64, 16, 1)
#         )

#     def forward(self, x):
#         return x + self.net(x)