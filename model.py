import torch
import torch.nn as nn

class NCA(nn.Module):
    def __init__(self):
        super().__init__()

        self.net = nn.Sequential(
            nn.Conv2d(16, 64, 1),
            nn.ReLU(),
            nn.Conv2d(64, 16, 1)
        )

    def forward(self, x):
        return x + self.net(x)