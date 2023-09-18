# %% Import torch
import torch

# %% Set device stuff
# setting device on GPU if available, else CPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("Using device:", device)
print()

# Additional Info when using cuda
if device.type == "cuda":
    with torch.cuda.device(device):
        info = torch.cuda.mem_get_info()
    print(torch.cuda.get_device_name(0))
    print("Memory Usage:")
    print("Total Available:", round(info[1] / 1024**3, 2), "GB")
    print("Globally Freed:", round(info[0] / 1024**3, 2), "GB")

# %%
