import torch
import numpy as np
from model import NCA
from utils import seed_grid

device = "cuda" if torch.cuda.is_available() else "cpu"

model = NCA().to(device)
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

for epoch in range(500):

    x = seed_grid().to(device)

    for i in range(50):
        x = model(x)

    loss = (x**2).mean()

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if epoch % 50 == 0:
        print("Epoch:", epoch, "Loss:", loss.item())

torch.save(model.state_dict(),"saved/nca.pth")
print("Model Saved")