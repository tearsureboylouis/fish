import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import numpy as np


# 自定义数据集
class FishDataset(Dataset):
    def __init__(self, observations, true_values):
        self.observations = observations
        self.true_values = true_values

    def __len__(self):
        return len(self.observations)

    def __getitem__(self, idx):
        return self.observations[idx], self.true_values[idx]


# 准备数据
observations = np.array([
    # 100
    [4, 7, 16, 19, 12, 16, 20, 20, 12, 6, 2, 1],
    [4, 6, 11, 17, 15, 7, 13, 14, 18, 18, 14, 1],
    [5, 3, 5, 3, 10, 11, 13, 11, 14, 16, 5, 1],
    [2, 3, 8, 12, 13, 10, 11, 11, 9, 8, 2, 3],

    # 150
    [3, 2, 5, 13, 18, 14, 14, 14, 12, 14, 16, 2],
    [21, 24, 21, 17, 10, 23, 18, 11, 11, 10, 4, 0],
    [3, 1, 5, 4, 4, 16, 22, 13, 10, 14, 19, 11],
    [14, 24, 12, 10, 14, 12, 7, 9, 8, 7, 8, 10],
    [3, 3, 7, 8, 10, 17, 13, 13, 12, 26, 14, 2],
    # 200
    [13, 7, 7, 2, 14, 30, 15, 10, 12, 19, 18, 15],
    [3, 1, 1, 7, 18, 15, 13, 15, 15, 12, 21, 8],
    [5, 17, 19, 19, 16, 18, 23, 30, 35, 18, 9, 6],
    [3, 6, 9, 17, 26, 12, 11, 20, 17, 21, 17, 2],
    [8, 13, 9, 15, 13, 17, 19, 27, 9, 9, 7, 6]
])

true_values = np.array([
    # 100
    [5.93, 10.37, 23.7, 28.15, 17.78, 23.7, 29.63, 29.63, 17.78, 8.89, 2.96, 1.48],
    [2.9, 4.35, 7.97, 12.32, 10.87, 5.07, 9.42, 10.14, 13.04, 13.04, 10.14, 0.72],
    [5.15, 3.09, 5.15, 3.09, 10.31, 11.34, 13.4, 11.34, 14.43, 16.49, 5.15, 1.03],
    [2.17, 3.26, 8.7, 13.04, 14.13, 10.87, 11.96, 11.96, 9.78, 8.7, 2.17, 3.26],
    # 150
    [3.54, 2.36, 5.91, 15.35, 21.26, 16.54, 16.54, 16.54, 14.17, 16.54, 18.9, 2.36],
    [18.53, 21.18, 18.53, 15.0, 8.82, 20.29, 15.88, 9.71, 9.71, 8.82, 3.53, 0.0],
    [3.69, 1.23, 6.15, 4.92, 4.92, 19.67, 27.05, 15.98, 12.3, 17.21, 23.36, 13.52],
    [15.56, 26.67, 13.33, 11.11, 15.56, 13.33, 7.78, 10.0, 8.89, 7.78, 8.89, 11.11],
    [3.52, 3.52, 8.2, 9.38, 11.72, 19.92, 15.23, 15.23, 14.06, 30.47, 16.41, 2.34],
    # 200
    [16.05, 8.64, 8.64, 2.47, 17.28, 37.04, 18.52, 12.35, 14.81, 23.46, 22.22, 18.52],
    [4.65, 1.55, 1.55, 10.85, 27.91, 23.26, 20.16, 23.26, 23.26, 18.6, 32.56, 12.4],
    [4.65, 15.81, 17.67, 17.67, 14.88, 16.74, 21.4, 27.91, 32.56, 16.74, 8.37, 5.58],
    [3.73, 7.45, 11.18, 21.12, 32.3, 14.91, 13.66, 24.84, 21.12, 26.09, 21.12, 2.48],
    [10.53, 17.11, 11.84, 19.74, 17.11, 22.37, 25.0, 35.53, 11.84, 11.84, 9.21, 7.89]
])

# 转换为PyTorch张量
observations = torch.FloatTensor(observations).unsqueeze(1)  # 形状变为 [9, 1, 12]
true_values = torch.FloatTensor(true_values)

# 创建数据集和数据加载器
dataset = FishDataset(observations, true_values)
train_loader = DataLoader(dataset, batch_size=3, shuffle=True)


# 定义卷积神经网络模型
class FishCNN(nn.Module):
    def __init__(self):
        super(FishCNN, self).__init__()
        self.conv1 = nn.Conv1d(1, 16, kernel_size=3, padding=1)
        self.conv2 = nn.Conv1d(16, 32, kernel_size=3, padding=1)
        self.fc1 = nn.Linear(32 * 12, 128)
        self.fc2 = nn.Linear(128, 12)
        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(0.2)

    def forward(self, x):
        x = self.relu(self.conv1(x))
        x = self.relu(self.conv2(x))
        x = x.view(-1, 32 * 12)
        x = self.dropout(self.relu(self.fc1(x)))
        x = self.fc2(x)
        return x


# 初始化模型、损失函数和优化器
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = FishCNN().to(device)
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# 训练模型
num_epochs = 1000
for epoch in range(num_epochs):
    model.train()
    total_loss = 0
    for batch_observations, batch_true_values in train_loader:
        batch_observations, batch_true_values = batch_observations.to(device), batch_true_values.to(device)

        optimizer.zero_grad()
        outputs = model(batch_observations)
        loss = criterion(outputs, batch_true_values)
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    avg_loss = total_loss / len(train_loader)
    if (epoch + 1) % 100 == 0:
        print(f'Epoch [{epoch + 1}/{num_epochs}], Loss: {avg_loss:.4f}')

model.eval()
with torch.no_grad():
    new_observations = torch.FloatTensor(observations).unsqueeze(1)
