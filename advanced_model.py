# advanced_model.py

import torch
import torch.nn as nn
import torch.nn.functional as F


class NeuralCA(nn.Module):
    """
    CPU Friendly Neural Cellular Automata
    """

    def __init__(self, channels=16, hidden=64, fire_rate=0.5):
        super().__init__()

        self.channels = channels
        self.fire_rate = fire_rate

        # Perception filters
        sobel_x = torch.tensor([
            [-1, 0, 1],
            [-2, 0, 2],
            [-1, 0, 1]
        ], dtype=torch.float32)

        sobel_y = sobel_x.t()

        identity = torch.tensor([
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ], dtype=torch.float32)

        self.register_buffer(
            "filters",
            torch.stack([identity, sobel_x, sobel_y])
        )

        # Update network
        self.fc0 = nn.Conv2d(channels * 3, hidden, 1)
        self.fc1 = nn.Conv2d(hidden, channels, 1)

        nn.init.zeros_(self.fc1.weight)
        nn.init.zeros_(self.fc1.bias)

    def perceive(self, x):
        """
        Apply perception filters
        """
        y = []

        for f in self.filters:
            f = f.view(1, 1, 3, 3).repeat(self.channels, 1, 1, 1)

            z = F.conv2d(
                x,
                f,
                padding=1,
                groups=self.channels
            )

            y.append(z)

        return torch.cat(y, dim=1)

    def forward(self, x):
        pre = self.perceive(x)

        dx = self.fc1(
            F.relu(
                self.fc0(pre)
            )
        )

        # stochastic update
        mask = (
            torch.rand(
                x[:, :1, :, :].shape,
                device=x.device
            ) <= self.fire_rate
        ).float()

        x = x + 0.1 * dx * mask
        x = torch.clamp(x, -3.0, 3.0)

        return x