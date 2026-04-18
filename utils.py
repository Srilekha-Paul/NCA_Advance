import torch

def seed_grid(size=64):
    x = torch.zeros(1,16,size,size)
    x[:,:,size//2,size//2] = 1.0
    return x