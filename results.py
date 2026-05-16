# results.py

import torch
import matplotlib.pyplot as plt
import pandas as pd

from advanced_model import NeuralCA
from utils import make_seed, calc_accuracy, damage_tensor
from targets import make_target_tensor


# =====================================================
# LOAD MODEL
# =====================================================
model = NeuralCA()

model.load_state_dict(
    torch.load("saved/best_model.pth", map_location="cpu")
)

model.eval()


# =====================================================
# TEST SETTINGS
# =====================================================
TARGETS = ["heart", "gecko", "emoji"]
ITERATIONS = 40

results = []


# =====================================================
# RUN TESTS
# =====================================================
for name in TARGETS:

    target = make_target_tensor(name)

    state = make_seed()

    with torch.no_grad():
        for _ in range(ITERATIONS):
            state = model(state)

    acc = calc_accuracy(state, target)

    # Damage + Heal Test
    damaged = damage_tensor(state)

    with torch.no_grad():
        for _ in range(20):
            damaged = model(damaged)

    heal_acc = calc_accuracy(damaged, target)

    results.append({
        "Target": name,
        "Growth Accuracy": round(acc, 2),
        "Healing Accuracy": round(heal_acc, 2)
    })


# =====================================================
# DATAFRAME
# =====================================================
df = pd.DataFrame(results)

print(df)

df.to_csv("paper_results.csv", index=False)


# =====================================================
# CHART
# =====================================================
plt.figure(figsize=(10, 6))

x = range(len(df))

plt.bar(
    [i - 0.15 for i in x],
    df["Growth Accuracy"],
    width=0.3,
    label="Growth"
)

plt.bar(
    [i + 0.15 for i in x],
    df["Healing Accuracy"],
    width=0.3,
    label="Healing"
)

plt.xticks(x, df["Target"])
plt.ylabel("Accuracy %")
plt.title("NCA Performance Results")
plt.legend()

plt.tight_layout()
plt.savefig("paper_results_chart.png", dpi=300)

print("✅ Results exported")
print("📄 paper_results.csv")
print("📊 paper_results_chart.png")