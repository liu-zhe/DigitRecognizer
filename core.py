from PIL import Image
import torch
from torch.utils.data import *
import torchvision.transforms as transforms
from myNet import *


def work(image_data):

    image = Image.open(image_data)
    image = image.convert('L')
    image.thumbnail((28, 28))
    transform = transforms.ToTensor()
    data = transform(image)
    data = data.reshape(1, 1, 28, 28)
    data = 1 - data
    print(data.shape)

    net = Net()
    net.load_state_dict(torch.load(
        'model.pth'))

    device = torch.device('cpu')
    net.to(device)

    net.eval()
    with torch.no_grad():
        data = data.to(device)
        outputs = net(data)
        print(outputs)
        _, ans = torch.max(outputs.data, 1)
    return ans.item()
