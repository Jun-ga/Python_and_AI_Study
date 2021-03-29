# -*- coding: utf-8 -*-
"""Untitled11.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1l_HLxueeXg8dx9p4AkYt9ukCScvEaoZt
"""

from __future__ import print_function

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
from torch.autograd import Variable

# Training settings
batch_size = 64                                                 # batch_size 64로 지정

# MNIST Dataset
train_dataset = datasets.MNIST(root='./mnist_data/',            # datasets를 통하여 MNIST데이터를 불러옴
                               train=True,                      # 훈련 데이터를 반환받음
                               transform=transforms.ToTensor(), # 현재 데이터를 파이토치 텐서로 변환
                               download=True)                   # 해당 경로에 MNIST데이터가 없다면 다운로드 받음
  
test_dataset = datasets.MNIST(root='./mnist_data/',             # datasets를 통하여 MNIST데이터를 불러옴
                              train=False,                      # 테스트 데이터를 반환받음
                              transform=transforms.ToTensor())  # 현재 데이터를 파이토치 텐서로 변환

# Data Loader (Input Pipeline)
train_loader = data.DataLoader(dataset=train_dataset,# dataloader를 사용하여 train_dataset를 불러오고, 64의 배치사이즈 지정, 셔플 사용
                                           batch_size=batch_size,
                                           shuffle=True)

test_loader = data.DataLoader(dataset=test_dataset, # dataloader를 사용하여 train_dataset를 불러오고, 64의 배치사이즈 지정, 셔플 사용X
                                          batch_size=batch_size,
                                          shuffle=False)


class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()                   #합성곱층  Conv2D와 MaxPool을 이용하여 구성한다.
        self.conv1 = nn.Conv2d(1, 10, kernel_size=5) # 인풋채널 1 아웃풋채널 10   kernel_size는 5x5 합성곱에 사용되는 필터 (=커널)의 크기입니다.
        self.conv2 = nn.Conv2d(10, 20, kernel_size=5) # 인풋채널 10 아웃풋채널 20   kernel_size는 5x5 합성곱에 사용되는 필터 (=커널)의 크기입니다.
        self.mp = nn.MaxPool2d(2)                     # 특정 영역에서 가장 큰 값을 샘플링하는 풀링 방식이며, 2x2
        self.fc = nn.Linear(320, 10)

    def forward(self, x):
        in_size = x.size(0)
        x = F.relu(self.mp(self.conv1(x)))
        x = F.relu(self.mp(self.conv2(x)))
        x = x.view(in_size, -1)  # flatten the tensor
        x = self.fc(x)
        return F.log_softmax(x) #결과값을 softmax 후 log값으로 출력

model = Net()    # model에 Net 클래스

optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.5)  # 최적화 함수로 경사하강법을 사용,모멘텀을 지정함으로
                                                                    #이전 이동값을 고려하여 일정비율만큼 다음값을 지정 (관성효과)


def train(epoch):
    model.train()
    for batch_idx, (data, target) in enumerate(train_loader):
        data, target = Variable(data), Variable(target) # Variable 클래스는 Tensor를 감싸고 있으며, Tensor에 정의된 거의 모든 연산을 지원합니다. 모든 계산을 마친 후에 .backward()를 호출하면, 자동으로 모든 기울기가 계산됩니다.
        optimizer.zero_grad()
        output = model(data)
        loss = F.nll_loss(output, target) # F.nll_loss()를 사용할 때는 원-핫 벡터를 넣을 필요없이 바로 실제값을 인자로 사용
        loss.backward()
        optimizer.step()
        if batch_idx % 10 == 0:
            print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                epoch, batch_idx * len(data), len(train_loader.dataset),
                100. * batch_idx / len(train_loader), loss.item()))


def test():
    model.eval()
    test_loss = 0
    correct = 0
    for data, target in test_loader:
        data, target = Variable(data, volatile=True), Variable(target) # backprop은 하지 않고 forward prop만 할 때 사용합니다
        output = model(data)
        # sum up batch loss
        test_loss += F.nll_loss(output, target, size_average=False).data
        # get the index of the max log-probability
        pred = output.data.max(1, keepdim=True)[1]
        correct += pred.eq(target.data.view_as(pred)).cpu().sum()

    test_loss /= len(test_loader.dataset)
    print('\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format(
        test_loss, correct, len(test_loader.dataset),
        100. * correct / len(test_loader.dataset)))


for epoch in range(1, 10):
    train(epoch)
    test()

