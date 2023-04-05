import torch.optim
import torchvision
import time
from pytorch_learning import Karen
from torch import nn
from torch.utils.data import DataLoader
from torch.nn import MaxPool2d, Sequential, Conv2d, Flatten, Linear

train_data = torchvision.datasets.CIFAR10("datasets", train=True, transform=torchvision.transforms.ToTensor(),
                                          download=True)
test_data = torchvision.datasets.CIFAR10("datasets", train=False, transform=torchvision.transforms.ToTensor(),
                                         download=True)
train_dataload = DataLoader(train_data, batch_size=64, shuffle=True)
test_dataload = DataLoader(test_data, batch_size=64, shuffle=True)

##创建网络模型
class Karen(nn.Module):
    def __init__(self):
        super(Karen, self).__init__()
        self.model1 = Sequential(Conv2d(3, 32, 5, stride=1, padding=2),
                                 MaxPool2d(2),
                                 Conv2d(32, 32, 5, stride=1, padding=2),
                                 MaxPool2d(2),
                                 Conv2d(32, 64, 5, stride=1, padding=2),
                                 MaxPool2d(2),
                                 Flatten(),
                                 Linear(1024, 64),
                                 Linear(64, 10)
                                 )

    def forward(self, input):
        output = self.model1(input)
        return output
karen = Karen()
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
train_loss = nn.CrossEntropyLoss()
train_loss = train_loss.cuda()
learning_rate = 1e-2
optim = torch.optim.SGD(karen.parameters(),learning_rate)

epoch = 20
train_step = 0
test_step = 0
###训练
for i in range(epoch):
    start_time = time.time()
    for data in train_dataload:
        imgs ,targets = data
        imgs = imgs.cuda()
        targets = targets.cuda()
        output = karen(imgs)
        optim.zero_grad()
        result_loss = train_loss(output,targets)
        result_loss.backward()
        optim.step()
        train_step += 1
        if train_step %100 ==0:
            end_time = time.time()
            print(end_time - start_time)
            print("----------第{}次训练loss:{}----------".format(train_step,result_loss))
###测试
    total_loss = 0
    total_accuracy = 0
    with torch.no_grad():
        for data in test_dataload:
            imgs,targets = data
            imgs = imgs.cuda()
            targets = targets.cuda()
            output = karen(imgs)
            test_loss = train_loss(output,targets)
            total_loss += test_loss
            accuracy = (output.argmax(1) == targets).sum().item()
            total_accuracy += accuracy
        acc = total_accuracy/len(test_data)
        test_step += 1
    print("----------第{}次测试loss:{}----------".format(test_step,total_loss))
    print("----------第{}次测试acc:{}----------".format(test_step,acc))
    ##模型保存
    #第一种
    # torch.save(karen,"karen_{}.pth".format(i+1))
    # #第二种
    # torch.save(karen.state_dict(),"karen_{}.pth".format(i+1))
