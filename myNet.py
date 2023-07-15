import torch.nn as nn


class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.features = nn.Sequential(
            nn.Conv2d(1, 96, 11, 1, 5), nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2),
            nn.Conv2d(96, 256, 5, 1, 2), nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2),
            nn.Conv2d(256, 384, 3, 1, 1), nn.ReLU(inplace=True),
            nn.Conv2d(384, 384, 3, 1, 1), nn.ReLU(inplace=True),
            nn.Conv2d(384, 256, 3, 1, 1), nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=3, stride=2),
            nn.Flatten(),
            nn.Linear(1024, 256), nn.ReLU(inplace=True),
            nn.Dropout(p=0.5),
            nn.Linear(256, 84), nn.ReLU(inplace=True),
            nn.Dropout(p=0.5),
            nn.Linear(84, 10)
        )

    def forward(self, x):
        x = self.features(x)
        return x
