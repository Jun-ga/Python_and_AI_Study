from torch import tensor
from torch import nn
from torch import sigmoid
import torch.optim as optim
import numpy as np

dataset_path="/content/drive/MyDrive/diabetes.csv"
dataset=np.loadtxt(dataset_path, delimiter=',',dtype=np.float32)
x_data=tensor(dataset[:,:-1])
y_data=tensor(dataset[:,[-1]])
#y_data=y_data.unsqueeze(1) 

count=0
ans=0
class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.linear = nn.Linear(8, 1)
    def forward(self, x):
        y_pred = sigmoid(self.linear(x))
        return y_pred

model = Model()
criterion = nn.BCELoss(reduction='mean')
optimizer = optim.SGD(model.parameters(), lr=0.08)

for epoch in range(1000):
    y_pred = model(x_data)
    loss = criterion(y_pred, y_data)
    print(f'Epoch {epoch + 1}/1000 | Loss: {loss.item():.4f}')
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

for i in range(len(y_data)):
    if y_pred[i] > 0.5:
        ans=1
    else:
        ans=0
    if ans==y_data[i]:
        count+=1

hour_var = tensor(x_data[0])
y_pred = model(hour_var)
print("Prediction (after training)", x_data[0],":", y_pred.item())
print("accuracy : ",(count/len(x_data))*100)

#결과
Epoch 1/1000 | Loss: 0.6688
Epoch 2/1000 | Loss: 0.6660
Epoch 3/1000 | Loss: 0.6634
Epoch 4/1000 | Loss: 0.6610
Epoch 5/1000 | Loss: 0.6587
Epoch 6/1000 | Loss: 0.6566
Epoch 7/1000 | Loss: 0.6545
Epoch 8/1000 | Loss: 0.6526
Epoch 9/1000 | Loss: 0.6508
Epoch 10/1000 | Loss: 0.6491
Epoch 11/1000 | Loss: 0.6474
Epoch 12/1000 | Loss: 0.6459
Epoch 13/1000 | Loss: 0.6444
Epoch 14/1000 | Loss: 0.6430
Epoch 15/1000 | Loss: 0.6416
Epoch 16/1000 | Loss: 0.6403
Epoch 17/1000 | Loss: 0.6391
Epoch 18/1000 | Loss: 0.6379
Epoch 19/1000 | Loss: 0.6367
Epoch 20/1000 | Loss: 0.6356
Epoch 21/1000 | Loss: 0.6345
Epoch 22/1000 | Loss: 0.6335
Epoch 23/1000 | Loss: 0.6325
Epoch 24/1000 | Loss: 0.6315
Epoch 25/1000 | Loss: 0.6305
Epoch 26/1000 | Loss: 0.6296
Epoch 27/1000 | Loss: 0.6287
Epoch 28/1000 | Loss: 0.6278
Epoch 29/1000 | Loss: 0.6269
Epoch 30/1000 | Loss: 0.6261
Epoch 31/1000 | Loss: 0.6253
Epoch 32/1000 | Loss: 0.6245
Epoch 33/1000 | Loss: 0.6237
Epoch 34/1000 | Loss: 0.6229
Epoch 35/1000 | Loss: 0.6221
Epoch 36/1000 | Loss: 0.6214
Epoch 37/1000 | Loss: 0.6206
Epoch 38/1000 | Loss: 0.6199
Epoch 39/1000 | Loss: 0.6192
Epoch 40/1000 | Loss: 0.6185
Epoch 41/1000 | Loss: 0.6178
Epoch 42/1000 | Loss: 0.6171
Epoch 43/1000 | Loss: 0.6164
Epoch 44/1000 | Loss: 0.6158
Epoch 45/1000 | Loss: 0.6151
Epoch 46/1000 | Loss: 0.6145
Epoch 47/1000 | Loss: 0.6138
Epoch 48/1000 | Loss: 0.6132
Epoch 49/1000 | Loss: 0.6125
Epoch 50/1000 | Loss: 0.6119
Epoch 51/1000 | Loss: 0.6113
Epoch 52/1000 | Loss: 0.6107
Epoch 53/1000 | Loss: 0.6101
Epoch 54/1000 | Loss: 0.6095
Epoch 55/1000 | Loss: 0.6089
Epoch 56/1000 | Loss: 0.6083
Epoch 57/1000 | Loss: 0.6077
Epoch 58/1000 | Loss: 0.6071
Epoch 59/1000 | Loss: 0.6065
Epoch 60/1000 | Loss: 0.6059
Epoch 61/1000 | Loss: 0.6053
Epoch 62/1000 | Loss: 0.6048
Epoch 63/1000 | Loss: 0.6042
Epoch 64/1000 | Loss: 0.6037
Epoch 65/1000 | Loss: 0.6031
Epoch 66/1000 | Loss: 0.6025
Epoch 67/1000 | Loss: 0.6020
Epoch 68/1000 | Loss: 0.6015
Epoch 69/1000 | Loss: 0.6009
Epoch 70/1000 | Loss: 0.6004
Epoch 71/1000 | Loss: 0.5998
Epoch 72/1000 | Loss: 0.5993
Epoch 73/1000 | Loss: 0.5988
Epoch 74/1000 | Loss: 0.5983
Epoch 75/1000 | Loss: 0.5977
Epoch 76/1000 | Loss: 0.5972
Epoch 77/1000 | Loss: 0.5967
Epoch 78/1000 | Loss: 0.5962
Epoch 79/1000 | Loss: 0.5957
Epoch 80/1000 | Loss: 0.5952
Epoch 81/1000 | Loss: 0.5947
Epoch 82/1000 | Loss: 0.5942
Epoch 83/1000 | Loss: 0.5937
Epoch 84/1000 | Loss: 0.5932
Epoch 85/1000 | Loss: 0.5927
Epoch 86/1000 | Loss: 0.5922
Epoch 87/1000 | Loss: 0.5917
Epoch 88/1000 | Loss: 0.5912
Epoch 89/1000 | Loss: 0.5908
Epoch 90/1000 | Loss: 0.5903
Epoch 91/1000 | Loss: 0.5898
Epoch 92/1000 | Loss: 0.5893
Epoch 93/1000 | Loss: 0.5889
Epoch 94/1000 | Loss: 0.5884
Epoch 95/1000 | Loss: 0.5879
Epoch 96/1000 | Loss: 0.5875
Epoch 97/1000 | Loss: 0.5870
Epoch 98/1000 | Loss: 0.5866
Epoch 99/1000 | Loss: 0.5861
Epoch 100/1000 | Loss: 0.5857
Epoch 101/1000 | Loss: 0.5852
Epoch 102/1000 | Loss: 0.5848
Epoch 103/1000 | Loss: 0.5843
Epoch 104/1000 | Loss: 0.5839
Epoch 105/1000 | Loss: 0.5834
Epoch 106/1000 | Loss: 0.5830
Epoch 107/1000 | Loss: 0.5826
Epoch 108/1000 | Loss: 0.5821
Epoch 109/1000 | Loss: 0.5817
Epoch 110/1000 | Loss: 0.5813
Epoch 111/1000 | Loss: 0.5808
Epoch 112/1000 | Loss: 0.5804
Epoch 113/1000 | Loss: 0.5800
Epoch 114/1000 | Loss: 0.5796
Epoch 115/1000 | Loss: 0.5792
Epoch 116/1000 | Loss: 0.5788
Epoch 117/1000 | Loss: 0.5783
Epoch 118/1000 | Loss: 0.5779
Epoch 119/1000 | Loss: 0.5775
Epoch 120/1000 | Loss: 0.5771
Epoch 121/1000 | Loss: 0.5767
Epoch 122/1000 | Loss: 0.5763
Epoch 123/1000 | Loss: 0.5759
Epoch 124/1000 | Loss: 0.5755
Epoch 125/1000 | Loss: 0.5751
Epoch 126/1000 | Loss: 0.5747
Epoch 127/1000 | Loss: 0.5743
Epoch 128/1000 | Loss: 0.5740
Epoch 129/1000 | Loss: 0.5736
Epoch 130/1000 | Loss: 0.5732
Epoch 131/1000 | Loss: 0.5728
Epoch 132/1000 | Loss: 0.5724
Epoch 133/1000 | Loss: 0.5720
Epoch 134/1000 | Loss: 0.5717
Epoch 135/1000 | Loss: 0.5713
Epoch 136/1000 | Loss: 0.5709
Epoch 137/1000 | Loss: 0.5706
Epoch 138/1000 | Loss: 0.5702
Epoch 139/1000 | Loss: 0.5698
Epoch 140/1000 | Loss: 0.5695
Epoch 141/1000 | Loss: 0.5691
Epoch 142/1000 | Loss: 0.5687
Epoch 143/1000 | Loss: 0.5684
Epoch 144/1000 | Loss: 0.5680
Epoch 145/1000 | Loss: 0.5677
Epoch 146/1000 | Loss: 0.5673
Epoch 147/1000 | Loss: 0.5670
Epoch 148/1000 | Loss: 0.5666
Epoch 149/1000 | Loss: 0.5663
Epoch 150/1000 | Loss: 0.5659
Epoch 151/1000 | Loss: 0.5656
Epoch 152/1000 | Loss: 0.5652
Epoch 153/1000 | Loss: 0.5649
Epoch 154/1000 | Loss: 0.5645
Epoch 155/1000 | Loss: 0.5642
Epoch 156/1000 | Loss: 0.5639
Epoch 157/1000 | Loss: 0.5635
Epoch 158/1000 | Loss: 0.5632
Epoch 159/1000 | Loss: 0.5629
Epoch 160/1000 | Loss: 0.5625
Epoch 161/1000 | Loss: 0.5622
Epoch 162/1000 | Loss: 0.5619
Epoch 163/1000 | Loss: 0.5616
Epoch 164/1000 | Loss: 0.5612
Epoch 165/1000 | Loss: 0.5609
Epoch 166/1000 | Loss: 0.5606
Epoch 167/1000 | Loss: 0.5603
Epoch 168/1000 | Loss: 0.5600
Epoch 169/1000 | Loss: 0.5597
Epoch 170/1000 | Loss: 0.5593
Epoch 171/1000 | Loss: 0.5590
Epoch 172/1000 | Loss: 0.5587
Epoch 173/1000 | Loss: 0.5584
Epoch 174/1000 | Loss: 0.5581
Epoch 175/1000 | Loss: 0.5578
Epoch 176/1000 | Loss: 0.5575
Epoch 177/1000 | Loss: 0.5572
Epoch 178/1000 | Loss: 0.5569
Epoch 179/1000 | Loss: 0.5566
Epoch 180/1000 | Loss: 0.5563
Epoch 181/1000 | Loss: 0.5560
Epoch 182/1000 | Loss: 0.5557
Epoch 183/1000 | Loss: 0.5554
Epoch 184/1000 | Loss: 0.5551
Epoch 185/1000 | Loss: 0.5548
Epoch 186/1000 | Loss: 0.5545
Epoch 187/1000 | Loss: 0.5543
Epoch 188/1000 | Loss: 0.5540
Epoch 189/1000 | Loss: 0.5537
Epoch 190/1000 | Loss: 0.5534
Epoch 191/1000 | Loss: 0.5531
Epoch 192/1000 | Loss: 0.5528
Epoch 193/1000 | Loss: 0.5526
Epoch 194/1000 | Loss: 0.5523
Epoch 195/1000 | Loss: 0.5520
Epoch 196/1000 | Loss: 0.5517
Epoch 197/1000 | Loss: 0.5515
Epoch 198/1000 | Loss: 0.5512
Epoch 199/1000 | Loss: 0.5509
Epoch 200/1000 | Loss: 0.5506
Epoch 201/1000 | Loss: 0.5504
Epoch 202/1000 | Loss: 0.5501
Epoch 203/1000 | Loss: 0.5498
Epoch 204/1000 | Loss: 0.5496
Epoch 205/1000 | Loss: 0.5493
Epoch 206/1000 | Loss: 0.5490
Epoch 207/1000 | Loss: 0.5488
Epoch 208/1000 | Loss: 0.5485
Epoch 209/1000 | Loss: 0.5483
Epoch 210/1000 | Loss: 0.5480
Epoch 211/1000 | Loss: 0.5478
Epoch 212/1000 | Loss: 0.5475
Epoch 213/1000 | Loss: 0.5472
Epoch 214/1000 | Loss: 0.5470
Epoch 215/1000 | Loss: 0.5467
Epoch 216/1000 | Loss: 0.5465
Epoch 217/1000 | Loss: 0.5462
Epoch 218/1000 | Loss: 0.5460
Epoch 219/1000 | Loss: 0.5458
Epoch 220/1000 | Loss: 0.5455
Epoch 221/1000 | Loss: 0.5453
Epoch 222/1000 | Loss: 0.5450
Epoch 223/1000 | Loss: 0.5448
Epoch 224/1000 | Loss: 0.5445
Epoch 225/1000 | Loss: 0.5443
Epoch 226/1000 | Loss: 0.5441
Epoch 227/1000 | Loss: 0.5438
Epoch 228/1000 | Loss: 0.5436
Epoch 229/1000 | Loss: 0.5433
Epoch 230/1000 | Loss: 0.5431
Epoch 231/1000 | Loss: 0.5429
Epoch 232/1000 | Loss: 0.5426
Epoch 233/1000 | Loss: 0.5424
Epoch 234/1000 | Loss: 0.5422
Epoch 235/1000 | Loss: 0.5420
Epoch 236/1000 | Loss: 0.5417
Epoch 237/1000 | Loss: 0.5415
Epoch 238/1000 | Loss: 0.5413
Epoch 239/1000 | Loss: 0.5411
Epoch 240/1000 | Loss: 0.5408
Epoch 241/1000 | Loss: 0.5406
Epoch 242/1000 | Loss: 0.5404
Epoch 243/1000 | Loss: 0.5402
Epoch 244/1000 | Loss: 0.5399
Epoch 245/1000 | Loss: 0.5397
Epoch 246/1000 | Loss: 0.5395
Epoch 247/1000 | Loss: 0.5393
Epoch 248/1000 | Loss: 0.5391
Epoch 249/1000 | Loss: 0.5389
Epoch 250/1000 | Loss: 0.5386
Epoch 251/1000 | Loss: 0.5384
Epoch 252/1000 | Loss: 0.5382
Epoch 253/1000 | Loss: 0.5380
Epoch 254/1000 | Loss: 0.5378
Epoch 255/1000 | Loss: 0.5376
Epoch 256/1000 | Loss: 0.5374
Epoch 257/1000 | Loss: 0.5372
Epoch 258/1000 | Loss: 0.5370
Epoch 259/1000 | Loss: 0.5368
Epoch 260/1000 | Loss: 0.5366
Epoch 261/1000 | Loss: 0.5364
Epoch 262/1000 | Loss: 0.5362
Epoch 263/1000 | Loss: 0.5360
Epoch 264/1000 | Loss: 0.5358
Epoch 265/1000 | Loss: 0.5356
Epoch 266/1000 | Loss: 0.5354
Epoch 267/1000 | Loss: 0.5352
Epoch 268/1000 | Loss: 0.5350
Epoch 269/1000 | Loss: 0.5348
Epoch 270/1000 | Loss: 0.5346
Epoch 271/1000 | Loss: 0.5344
Epoch 272/1000 | Loss: 0.5342
Epoch 273/1000 | Loss: 0.5340
Epoch 274/1000 | Loss: 0.5338
Epoch 275/1000 | Loss: 0.5336
Epoch 276/1000 | Loss: 0.5334
Epoch 277/1000 | Loss: 0.5332
Epoch 278/1000 | Loss: 0.5330
Epoch 279/1000 | Loss: 0.5329
Epoch 280/1000 | Loss: 0.5327
Epoch 281/1000 | Loss: 0.5325
Epoch 282/1000 | Loss: 0.5323
Epoch 283/1000 | Loss: 0.5321
Epoch 284/1000 | Loss: 0.5319
Epoch 285/1000 | Loss: 0.5317
Epoch 286/1000 | Loss: 0.5316
Epoch 287/1000 | Loss: 0.5314
Epoch 288/1000 | Loss: 0.5312
Epoch 289/1000 | Loss: 0.5310
Epoch 290/1000 | Loss: 0.5308
Epoch 291/1000 | Loss: 0.5307
Epoch 292/1000 | Loss: 0.5305
Epoch 293/1000 | Loss: 0.5303
Epoch 294/1000 | Loss: 0.5301
Epoch 295/1000 | Loss: 0.5300
Epoch 296/1000 | Loss: 0.5298
Epoch 297/1000 | Loss: 0.5296
Epoch 298/1000 | Loss: 0.5294
Epoch 299/1000 | Loss: 0.5293
Epoch 300/1000 | Loss: 0.5291
Epoch 301/1000 | Loss: 0.5289
Epoch 302/1000 | Loss: 0.5287
Epoch 303/1000 | Loss: 0.5286
Epoch 304/1000 | Loss: 0.5284
Epoch 305/1000 | Loss: 0.5282
Epoch 306/1000 | Loss: 0.5281
Epoch 307/1000 | Loss: 0.5279
Epoch 308/1000 | Loss: 0.5277
Epoch 309/1000 | Loss: 0.5276
Epoch 310/1000 | Loss: 0.5274
Epoch 311/1000 | Loss: 0.5272
Epoch 312/1000 | Loss: 0.5271
Epoch 313/1000 | Loss: 0.5269
Epoch 314/1000 | Loss: 0.5268
Epoch 315/1000 | Loss: 0.5266
Epoch 316/1000 | Loss: 0.5264
Epoch 317/1000 | Loss: 0.5263
Epoch 318/1000 | Loss: 0.5261
Epoch 319/1000 | Loss: 0.5260
Epoch 320/1000 | Loss: 0.5258
Epoch 321/1000 | Loss: 0.5256
Epoch 322/1000 | Loss: 0.5255
Epoch 323/1000 | Loss: 0.5253
Epoch 324/1000 | Loss: 0.5252
Epoch 325/1000 | Loss: 0.5250
Epoch 326/1000 | Loss: 0.5249
Epoch 327/1000 | Loss: 0.5247
Epoch 328/1000 | Loss: 0.5246
Epoch 329/1000 | Loss: 0.5244
Epoch 330/1000 | Loss: 0.5243
Epoch 331/1000 | Loss: 0.5241
Epoch 332/1000 | Loss: 0.5240
Epoch 333/1000 | Loss: 0.5238
Epoch 334/1000 | Loss: 0.5237
Epoch 335/1000 | Loss: 0.5235
Epoch 336/1000 | Loss: 0.5234
Epoch 337/1000 | Loss: 0.5232
Epoch 338/1000 | Loss: 0.5231
Epoch 339/1000 | Loss: 0.5229
Epoch 340/1000 | Loss: 0.5228
Epoch 341/1000 | Loss: 0.5226
Epoch 342/1000 | Loss: 0.5225
Epoch 343/1000 | Loss: 0.5223
Epoch 344/1000 | Loss: 0.5222
Epoch 345/1000 | Loss: 0.5221
Epoch 346/1000 | Loss: 0.5219
Epoch 347/1000 | Loss: 0.5218
Epoch 348/1000 | Loss: 0.5216
Epoch 349/1000 | Loss: 0.5215
Epoch 350/1000 | Loss: 0.5213
Epoch 351/1000 | Loss: 0.5212
Epoch 352/1000 | Loss: 0.5211
Epoch 353/1000 | Loss: 0.5209
Epoch 354/1000 | Loss: 0.5208
Epoch 355/1000 | Loss: 0.5207
Epoch 356/1000 | Loss: 0.5205
Epoch 357/1000 | Loss: 0.5204
Epoch 358/1000 | Loss: 0.5202
Epoch 359/1000 | Loss: 0.5201
Epoch 360/1000 | Loss: 0.5200
Epoch 361/1000 | Loss: 0.5198
Epoch 362/1000 | Loss: 0.5197
Epoch 363/1000 | Loss: 0.5196
Epoch 364/1000 | Loss: 0.5194
Epoch 365/1000 | Loss: 0.5193
Epoch 366/1000 | Loss: 0.5192
Epoch 367/1000 | Loss: 0.5190
Epoch 368/1000 | Loss: 0.5189
Epoch 369/1000 | Loss: 0.5188
Epoch 370/1000 | Loss: 0.5187
Epoch 371/1000 | Loss: 0.5185
Epoch 372/1000 | Loss: 0.5184
Epoch 373/1000 | Loss: 0.5183
Epoch 374/1000 | Loss: 0.5181
Epoch 375/1000 | Loss: 0.5180
Epoch 376/1000 | Loss: 0.5179
Epoch 377/1000 | Loss: 0.5178
Epoch 378/1000 | Loss: 0.5176
Epoch 379/1000 | Loss: 0.5175
Epoch 380/1000 | Loss: 0.5174
Epoch 381/1000 | Loss: 0.5173
Epoch 382/1000 | Loss: 0.5171
Epoch 383/1000 | Loss: 0.5170
Epoch 384/1000 | Loss: 0.5169
Epoch 385/1000 | Loss: 0.5168
Epoch 386/1000 | Loss: 0.5167
Epoch 387/1000 | Loss: 0.5165
Epoch 388/1000 | Loss: 0.5164
Epoch 389/1000 | Loss: 0.5163
Epoch 390/1000 | Loss: 0.5162
Epoch 391/1000 | Loss: 0.5161
Epoch 392/1000 | Loss: 0.5159
Epoch 393/1000 | Loss: 0.5158
Epoch 394/1000 | Loss: 0.5157
Epoch 395/1000 | Loss: 0.5156
Epoch 396/1000 | Loss: 0.5155
Epoch 397/1000 | Loss: 0.5153
Epoch 398/1000 | Loss: 0.5152
Epoch 399/1000 | Loss: 0.5151
Epoch 400/1000 | Loss: 0.5150
Epoch 401/1000 | Loss: 0.5149
Epoch 402/1000 | Loss: 0.5148
Epoch 403/1000 | Loss: 0.5147
Epoch 404/1000 | Loss: 0.5145
Epoch 405/1000 | Loss: 0.5144
Epoch 406/1000 | Loss: 0.5143
Epoch 407/1000 | Loss: 0.5142
Epoch 408/1000 | Loss: 0.5141
Epoch 409/1000 | Loss: 0.5140
Epoch 410/1000 | Loss: 0.5139
Epoch 411/1000 | Loss: 0.5138
Epoch 412/1000 | Loss: 0.5136
Epoch 413/1000 | Loss: 0.5135
Epoch 414/1000 | Loss: 0.5134
Epoch 415/1000 | Loss: 0.5133
Epoch 416/1000 | Loss: 0.5132
Epoch 417/1000 | Loss: 0.5131
Epoch 418/1000 | Loss: 0.5130
Epoch 419/1000 | Loss: 0.5129
Epoch 420/1000 | Loss: 0.5128
Epoch 421/1000 | Loss: 0.5127
Epoch 422/1000 | Loss: 0.5126
Epoch 423/1000 | Loss: 0.5125
Epoch 424/1000 | Loss: 0.5123
Epoch 425/1000 | Loss: 0.5122
Epoch 426/1000 | Loss: 0.5121
Epoch 427/1000 | Loss: 0.5120
Epoch 428/1000 | Loss: 0.5119
Epoch 429/1000 | Loss: 0.5118
Epoch 430/1000 | Loss: 0.5117
Epoch 431/1000 | Loss: 0.5116
Epoch 432/1000 | Loss: 0.5115
Epoch 433/1000 | Loss: 0.5114
Epoch 434/1000 | Loss: 0.5113
Epoch 435/1000 | Loss: 0.5112
Epoch 436/1000 | Loss: 0.5111
Epoch 437/1000 | Loss: 0.5110
Epoch 438/1000 | Loss: 0.5109
Epoch 439/1000 | Loss: 0.5108
Epoch 440/1000 | Loss: 0.5107
Epoch 441/1000 | Loss: 0.5106
Epoch 442/1000 | Loss: 0.5105
Epoch 443/1000 | Loss: 0.5104
Epoch 444/1000 | Loss: 0.5103
Epoch 445/1000 | Loss: 0.5102
Epoch 446/1000 | Loss: 0.5101
Epoch 447/1000 | Loss: 0.5100
Epoch 448/1000 | Loss: 0.5099
Epoch 449/1000 | Loss: 0.5098
Epoch 450/1000 | Loss: 0.5097
Epoch 451/1000 | Loss: 0.5096
Epoch 452/1000 | Loss: 0.5095
Epoch 453/1000 | Loss: 0.5094
Epoch 454/1000 | Loss: 0.5093
Epoch 455/1000 | Loss: 0.5092
Epoch 456/1000 | Loss: 0.5092
Epoch 457/1000 | Loss: 0.5091
Epoch 458/1000 | Loss: 0.5090
Epoch 459/1000 | Loss: 0.5089
Epoch 460/1000 | Loss: 0.5088
Epoch 461/1000 | Loss: 0.5087
Epoch 462/1000 | Loss: 0.5086
Epoch 463/1000 | Loss: 0.5085
Epoch 464/1000 | Loss: 0.5084
Epoch 465/1000 | Loss: 0.5083
Epoch 466/1000 | Loss: 0.5082
Epoch 467/1000 | Loss: 0.5081
Epoch 468/1000 | Loss: 0.5080
Epoch 469/1000 | Loss: 0.5080
Epoch 470/1000 | Loss: 0.5079
Epoch 471/1000 | Loss: 0.5078
Epoch 472/1000 | Loss: 0.5077
Epoch 473/1000 | Loss: 0.5076
Epoch 474/1000 | Loss: 0.5075
Epoch 475/1000 | Loss: 0.5074
Epoch 476/1000 | Loss: 0.5073
Epoch 477/1000 | Loss: 0.5072
Epoch 478/1000 | Loss: 0.5072
Epoch 479/1000 | Loss: 0.5071
Epoch 480/1000 | Loss: 0.5070
Epoch 481/1000 | Loss: 0.5069
Epoch 482/1000 | Loss: 0.5068
Epoch 483/1000 | Loss: 0.5067
Epoch 484/1000 | Loss: 0.5066
Epoch 485/1000 | Loss: 0.5066
Epoch 486/1000 | Loss: 0.5065
Epoch 487/1000 | Loss: 0.5064
Epoch 488/1000 | Loss: 0.5063
Epoch 489/1000 | Loss: 0.5062
Epoch 490/1000 | Loss: 0.5061
Epoch 491/1000 | Loss: 0.5060
Epoch 492/1000 | Loss: 0.5060
Epoch 493/1000 | Loss: 0.5059
Epoch 494/1000 | Loss: 0.5058
Epoch 495/1000 | Loss: 0.5057
Epoch 496/1000 | Loss: 0.5056
Epoch 497/1000 | Loss: 0.5055
Epoch 498/1000 | Loss: 0.5055
Epoch 499/1000 | Loss: 0.5054
Epoch 500/1000 | Loss: 0.5053
Epoch 501/1000 | Loss: 0.5052
Epoch 502/1000 | Loss: 0.5051
Epoch 503/1000 | Loss: 0.5051
Epoch 504/1000 | Loss: 0.5050
Epoch 505/1000 | Loss: 0.5049
Epoch 506/1000 | Loss: 0.5048
Epoch 507/1000 | Loss: 0.5047
Epoch 508/1000 | Loss: 0.5047
Epoch 509/1000 | Loss: 0.5046
Epoch 510/1000 | Loss: 0.5045
Epoch 511/1000 | Loss: 0.5044
Epoch 512/1000 | Loss: 0.5043
Epoch 513/1000 | Loss: 0.5043
Epoch 514/1000 | Loss: 0.5042
Epoch 515/1000 | Loss: 0.5041
Epoch 516/1000 | Loss: 0.5040
Epoch 517/1000 | Loss: 0.5040
Epoch 518/1000 | Loss: 0.5039
Epoch 519/1000 | Loss: 0.5038
Epoch 520/1000 | Loss: 0.5037
Epoch 521/1000 | Loss: 0.5037
Epoch 522/1000 | Loss: 0.5036
Epoch 523/1000 | Loss: 0.5035
Epoch 524/1000 | Loss: 0.5034
Epoch 525/1000 | Loss: 0.5034
Epoch 526/1000 | Loss: 0.5033
Epoch 527/1000 | Loss: 0.5032
Epoch 528/1000 | Loss: 0.5031
Epoch 529/1000 | Loss: 0.5031
Epoch 530/1000 | Loss: 0.5030
Epoch 531/1000 | Loss: 0.5029
Epoch 532/1000 | Loss: 0.5028
Epoch 533/1000 | Loss: 0.5028
Epoch 534/1000 | Loss: 0.5027
Epoch 535/1000 | Loss: 0.5026
Epoch 536/1000 | Loss: 0.5025
Epoch 537/1000 | Loss: 0.5025
Epoch 538/1000 | Loss: 0.5024
Epoch 539/1000 | Loss: 0.5023
Epoch 540/1000 | Loss: 0.5023
Epoch 541/1000 | Loss: 0.5022
Epoch 542/1000 | Loss: 0.5021
Epoch 543/1000 | Loss: 0.5020
Epoch 544/1000 | Loss: 0.5020
Epoch 545/1000 | Loss: 0.5019
Epoch 546/1000 | Loss: 0.5018
Epoch 547/1000 | Loss: 0.5018
Epoch 548/1000 | Loss: 0.5017
Epoch 549/1000 | Loss: 0.5016
Epoch 550/1000 | Loss: 0.5016
Epoch 551/1000 | Loss: 0.5015
Epoch 552/1000 | Loss: 0.5014
Epoch 553/1000 | Loss: 0.5013
Epoch 554/1000 | Loss: 0.5013
Epoch 555/1000 | Loss: 0.5012
Epoch 556/1000 | Loss: 0.5011
Epoch 557/1000 | Loss: 0.5011
Epoch 558/1000 | Loss: 0.5010
Epoch 559/1000 | Loss: 0.5009
Epoch 560/1000 | Loss: 0.5009
Epoch 561/1000 | Loss: 0.5008
Epoch 562/1000 | Loss: 0.5007
Epoch 563/1000 | Loss: 0.5007
Epoch 564/1000 | Loss: 0.5006
Epoch 565/1000 | Loss: 0.5005
Epoch 566/1000 | Loss: 0.5005
Epoch 567/1000 | Loss: 0.5004
Epoch 568/1000 | Loss: 0.5003
Epoch 569/1000 | Loss: 0.5003
Epoch 570/1000 | Loss: 0.5002
Epoch 571/1000 | Loss: 0.5002
Epoch 572/1000 | Loss: 0.5001
Epoch 573/1000 | Loss: 0.5000
Epoch 574/1000 | Loss: 0.5000
Epoch 575/1000 | Loss: 0.4999
Epoch 576/1000 | Loss: 0.4998
Epoch 577/1000 | Loss: 0.4998
Epoch 578/1000 | Loss: 0.4997
Epoch 579/1000 | Loss: 0.4996
Epoch 580/1000 | Loss: 0.4996
Epoch 581/1000 | Loss: 0.4995
Epoch 582/1000 | Loss: 0.4995
Epoch 583/1000 | Loss: 0.4994
Epoch 584/1000 | Loss: 0.4993
Epoch 585/1000 | Loss: 0.4993
Epoch 586/1000 | Loss: 0.4992
Epoch 587/1000 | Loss: 0.4991
Epoch 588/1000 | Loss: 0.4991
Epoch 589/1000 | Loss: 0.4990
Epoch 590/1000 | Loss: 0.4990
Epoch 591/1000 | Loss: 0.4989
Epoch 592/1000 | Loss: 0.4988
Epoch 593/1000 | Loss: 0.4988
Epoch 594/1000 | Loss: 0.4987
Epoch 595/1000 | Loss: 0.4987
Epoch 596/1000 | Loss: 0.4986
Epoch 597/1000 | Loss: 0.4985
Epoch 598/1000 | Loss: 0.4985
Epoch 599/1000 | Loss: 0.4984
Epoch 600/1000 | Loss: 0.4984
Epoch 601/1000 | Loss: 0.4983
Epoch 602/1000 | Loss: 0.4982
Epoch 603/1000 | Loss: 0.4982
Epoch 604/1000 | Loss: 0.4981
Epoch 605/1000 | Loss: 0.4981
Epoch 606/1000 | Loss: 0.4980
Epoch 607/1000 | Loss: 0.4979
Epoch 608/1000 | Loss: 0.4979
Epoch 609/1000 | Loss: 0.4978
Epoch 610/1000 | Loss: 0.4978
Epoch 611/1000 | Loss: 0.4977
Epoch 612/1000 | Loss: 0.4977
Epoch 613/1000 | Loss: 0.4976
Epoch 614/1000 | Loss: 0.4975
Epoch 615/1000 | Loss: 0.4975
Epoch 616/1000 | Loss: 0.4974
Epoch 617/1000 | Loss: 0.4974
Epoch 618/1000 | Loss: 0.4973
Epoch 619/1000 | Loss: 0.4973
Epoch 620/1000 | Loss: 0.4972
Epoch 621/1000 | Loss: 0.4971
Epoch 622/1000 | Loss: 0.4971
Epoch 623/1000 | Loss: 0.4970
Epoch 624/1000 | Loss: 0.4970
Epoch 625/1000 | Loss: 0.4969
Epoch 626/1000 | Loss: 0.4969
Epoch 627/1000 | Loss: 0.4968
Epoch 628/1000 | Loss: 0.4968
Epoch 629/1000 | Loss: 0.4967
Epoch 630/1000 | Loss: 0.4967
Epoch 631/1000 | Loss: 0.4966
Epoch 632/1000 | Loss: 0.4965
Epoch 633/1000 | Loss: 0.4965
Epoch 634/1000 | Loss: 0.4964
Epoch 635/1000 | Loss: 0.4964
Epoch 636/1000 | Loss: 0.4963
Epoch 637/1000 | Loss: 0.4963
Epoch 638/1000 | Loss: 0.4962
Epoch 639/1000 | Loss: 0.4962
Epoch 640/1000 | Loss: 0.4961
Epoch 641/1000 | Loss: 0.4961
Epoch 642/1000 | Loss: 0.4960
Epoch 643/1000 | Loss: 0.4960
Epoch 644/1000 | Loss: 0.4959
Epoch 645/1000 | Loss: 0.4959
Epoch 646/1000 | Loss: 0.4958
Epoch 647/1000 | Loss: 0.4958
Epoch 648/1000 | Loss: 0.4957
Epoch 649/1000 | Loss: 0.4957
Epoch 650/1000 | Loss: 0.4956
Epoch 651/1000 | Loss: 0.4955
Epoch 652/1000 | Loss: 0.4955
Epoch 653/1000 | Loss: 0.4954
Epoch 654/1000 | Loss: 0.4954
Epoch 655/1000 | Loss: 0.4953
Epoch 656/1000 | Loss: 0.4953
Epoch 657/1000 | Loss: 0.4952
Epoch 658/1000 | Loss: 0.4952
Epoch 659/1000 | Loss: 0.4951
Epoch 660/1000 | Loss: 0.4951
Epoch 661/1000 | Loss: 0.4950
Epoch 662/1000 | Loss: 0.4950
Epoch 663/1000 | Loss: 0.4949
Epoch 664/1000 | Loss: 0.4949
Epoch 665/1000 | Loss: 0.4948
Epoch 666/1000 | Loss: 0.4948
Epoch 667/1000 | Loss: 0.4947
Epoch 668/1000 | Loss: 0.4947
Epoch 669/1000 | Loss: 0.4947
Epoch 670/1000 | Loss: 0.4946
Epoch 671/1000 | Loss: 0.4946
Epoch 672/1000 | Loss: 0.4945
Epoch 673/1000 | Loss: 0.4945
Epoch 674/1000 | Loss: 0.4944
Epoch 675/1000 | Loss: 0.4944
Epoch 676/1000 | Loss: 0.4943
Epoch 677/1000 | Loss: 0.4943
Epoch 678/1000 | Loss: 0.4942
Epoch 679/1000 | Loss: 0.4942
Epoch 680/1000 | Loss: 0.4941
Epoch 681/1000 | Loss: 0.4941
Epoch 682/1000 | Loss: 0.4940
Epoch 683/1000 | Loss: 0.4940
Epoch 684/1000 | Loss: 0.4939
Epoch 685/1000 | Loss: 0.4939
Epoch 686/1000 | Loss: 0.4938
Epoch 687/1000 | Loss: 0.4938
Epoch 688/1000 | Loss: 0.4938
Epoch 689/1000 | Loss: 0.4937
Epoch 690/1000 | Loss: 0.4937
Epoch 691/1000 | Loss: 0.4936
Epoch 692/1000 | Loss: 0.4936
Epoch 693/1000 | Loss: 0.4935
Epoch 694/1000 | Loss: 0.4935
Epoch 695/1000 | Loss: 0.4934
Epoch 696/1000 | Loss: 0.4934
Epoch 697/1000 | Loss: 0.4933
Epoch 698/1000 | Loss: 0.4933
Epoch 699/1000 | Loss: 0.4933
Epoch 700/1000 | Loss: 0.4932
Epoch 701/1000 | Loss: 0.4932
Epoch 702/1000 | Loss: 0.4931
Epoch 703/1000 | Loss: 0.4931
Epoch 704/1000 | Loss: 0.4930
Epoch 705/1000 | Loss: 0.4930
Epoch 706/1000 | Loss: 0.4929
Epoch 707/1000 | Loss: 0.4929
Epoch 708/1000 | Loss: 0.4929
Epoch 709/1000 | Loss: 0.4928
Epoch 710/1000 | Loss: 0.4928
Epoch 711/1000 | Loss: 0.4927
Epoch 712/1000 | Loss: 0.4927
Epoch 713/1000 | Loss: 0.4926
Epoch 714/1000 | Loss: 0.4926
Epoch 715/1000 | Loss: 0.4926
Epoch 716/1000 | Loss: 0.4925
Epoch 717/1000 | Loss: 0.4925
Epoch 718/1000 | Loss: 0.4924
Epoch 719/1000 | Loss: 0.4924
Epoch 720/1000 | Loss: 0.4923
Epoch 721/1000 | Loss: 0.4923
Epoch 722/1000 | Loss: 0.4923
Epoch 723/1000 | Loss: 0.4922
Epoch 724/1000 | Loss: 0.4922
Epoch 725/1000 | Loss: 0.4921
Epoch 726/1000 | Loss: 0.4921
Epoch 727/1000 | Loss: 0.4921
Epoch 728/1000 | Loss: 0.4920
Epoch 729/1000 | Loss: 0.4920
Epoch 730/1000 | Loss: 0.4919
Epoch 731/1000 | Loss: 0.4919
Epoch 732/1000 | Loss: 0.4918
Epoch 733/1000 | Loss: 0.4918
Epoch 734/1000 | Loss: 0.4918
Epoch 735/1000 | Loss: 0.4917
Epoch 736/1000 | Loss: 0.4917
Epoch 737/1000 | Loss: 0.4916
Epoch 738/1000 | Loss: 0.4916
Epoch 739/1000 | Loss: 0.4916
Epoch 740/1000 | Loss: 0.4915
Epoch 741/1000 | Loss: 0.4915
Epoch 742/1000 | Loss: 0.4914
Epoch 743/1000 | Loss: 0.4914
Epoch 744/1000 | Loss: 0.4914
Epoch 745/1000 | Loss: 0.4913
Epoch 746/1000 | Loss: 0.4913
Epoch 747/1000 | Loss: 0.4912
Epoch 748/1000 | Loss: 0.4912
Epoch 749/1000 | Loss: 0.4912
Epoch 750/1000 | Loss: 0.4911
Epoch 751/1000 | Loss: 0.4911
Epoch 752/1000 | Loss: 0.4911
Epoch 753/1000 | Loss: 0.4910
Epoch 754/1000 | Loss: 0.4910
Epoch 755/1000 | Loss: 0.4909
Epoch 756/1000 | Loss: 0.4909
Epoch 757/1000 | Loss: 0.4909
Epoch 758/1000 | Loss: 0.4908
Epoch 759/1000 | Loss: 0.4908
Epoch 760/1000 | Loss: 0.4907
Epoch 761/1000 | Loss: 0.4907
Epoch 762/1000 | Loss: 0.4907
Epoch 763/1000 | Loss: 0.4906
Epoch 764/1000 | Loss: 0.4906
Epoch 765/1000 | Loss: 0.4906
Epoch 766/1000 | Loss: 0.4905
Epoch 767/1000 | Loss: 0.4905
Epoch 768/1000 | Loss: 0.4904
Epoch 769/1000 | Loss: 0.4904
Epoch 770/1000 | Loss: 0.4904
Epoch 771/1000 | Loss: 0.4903
Epoch 772/1000 | Loss: 0.4903
Epoch 773/1000 | Loss: 0.4903
Epoch 774/1000 | Loss: 0.4902
Epoch 775/1000 | Loss: 0.4902
Epoch 776/1000 | Loss: 0.4902
Epoch 777/1000 | Loss: 0.4901
Epoch 778/1000 | Loss: 0.4901
Epoch 779/1000 | Loss: 0.4900
Epoch 780/1000 | Loss: 0.4900
Epoch 781/1000 | Loss: 0.4900
Epoch 782/1000 | Loss: 0.4899
Epoch 783/1000 | Loss: 0.4899
Epoch 784/1000 | Loss: 0.4899
Epoch 785/1000 | Loss: 0.4898
Epoch 786/1000 | Loss: 0.4898
Epoch 787/1000 | Loss: 0.4898
Epoch 788/1000 | Loss: 0.4897
Epoch 789/1000 | Loss: 0.4897
Epoch 790/1000 | Loss: 0.4897
Epoch 791/1000 | Loss: 0.4896
Epoch 792/1000 | Loss: 0.4896
Epoch 793/1000 | Loss: 0.4895
Epoch 794/1000 | Loss: 0.4895
Epoch 795/1000 | Loss: 0.4895
Epoch 796/1000 | Loss: 0.4894
Epoch 797/1000 | Loss: 0.4894
Epoch 798/1000 | Loss: 0.4894
Epoch 799/1000 | Loss: 0.4893
Epoch 800/1000 | Loss: 0.4893
Epoch 801/1000 | Loss: 0.4893
Epoch 802/1000 | Loss: 0.4892
Epoch 803/1000 | Loss: 0.4892
Epoch 804/1000 | Loss: 0.4892
Epoch 805/1000 | Loss: 0.4891
Epoch 806/1000 | Loss: 0.4891
Epoch 807/1000 | Loss: 0.4891
Epoch 808/1000 | Loss: 0.4890
Epoch 809/1000 | Loss: 0.4890
Epoch 810/1000 | Loss: 0.4890
Epoch 811/1000 | Loss: 0.4889
Epoch 812/1000 | Loss: 0.4889
Epoch 813/1000 | Loss: 0.4889
Epoch 814/1000 | Loss: 0.4888
Epoch 815/1000 | Loss: 0.4888
Epoch 816/1000 | Loss: 0.4888
Epoch 817/1000 | Loss: 0.4887
Epoch 818/1000 | Loss: 0.4887
Epoch 819/1000 | Loss: 0.4887
Epoch 820/1000 | Loss: 0.4886
Epoch 821/1000 | Loss: 0.4886
Epoch 822/1000 | Loss: 0.4886
Epoch 823/1000 | Loss: 0.4885
Epoch 824/1000 | Loss: 0.4885
Epoch 825/1000 | Loss: 0.4885
Epoch 826/1000 | Loss: 0.4884
Epoch 827/1000 | Loss: 0.4884
Epoch 828/1000 | Loss: 0.4884
Epoch 829/1000 | Loss: 0.4884
Epoch 830/1000 | Loss: 0.4883
Epoch 831/1000 | Loss: 0.4883
Epoch 832/1000 | Loss: 0.4883
Epoch 833/1000 | Loss: 0.4882
Epoch 834/1000 | Loss: 0.4882
Epoch 835/1000 | Loss: 0.4882
Epoch 836/1000 | Loss: 0.4881
Epoch 837/1000 | Loss: 0.4881
Epoch 838/1000 | Loss: 0.4881
Epoch 839/1000 | Loss: 0.4880
Epoch 840/1000 | Loss: 0.4880
Epoch 841/1000 | Loss: 0.4880
Epoch 842/1000 | Loss: 0.4879
Epoch 843/1000 | Loss: 0.4879
Epoch 844/1000 | Loss: 0.4879
Epoch 845/1000 | Loss: 0.4879
Epoch 846/1000 | Loss: 0.4878
Epoch 847/1000 | Loss: 0.4878
Epoch 848/1000 | Loss: 0.4878
Epoch 849/1000 | Loss: 0.4877
Epoch 850/1000 | Loss: 0.4877
Epoch 851/1000 | Loss: 0.4877
Epoch 852/1000 | Loss: 0.4876
Epoch 853/1000 | Loss: 0.4876
Epoch 854/1000 | Loss: 0.4876
Epoch 855/1000 | Loss: 0.4876
Epoch 856/1000 | Loss: 0.4875
Epoch 857/1000 | Loss: 0.4875
Epoch 858/1000 | Loss: 0.4875
Epoch 859/1000 | Loss: 0.4874
Epoch 860/1000 | Loss: 0.4874
Epoch 861/1000 | Loss: 0.4874
Epoch 862/1000 | Loss: 0.4873
Epoch 863/1000 | Loss: 0.4873
Epoch 864/1000 | Loss: 0.4873
Epoch 865/1000 | Loss: 0.4873
Epoch 866/1000 | Loss: 0.4872
Epoch 867/1000 | Loss: 0.4872
Epoch 868/1000 | Loss: 0.4872
Epoch 869/1000 | Loss: 0.4871
Epoch 870/1000 | Loss: 0.4871
Epoch 871/1000 | Loss: 0.4871
Epoch 872/1000 | Loss: 0.4871
Epoch 873/1000 | Loss: 0.4870
Epoch 874/1000 | Loss: 0.4870
Epoch 875/1000 | Loss: 0.4870
Epoch 876/1000 | Loss: 0.4869
Epoch 877/1000 | Loss: 0.4869
Epoch 878/1000 | Loss: 0.4869
Epoch 879/1000 | Loss: 0.4869
Epoch 880/1000 | Loss: 0.4868
Epoch 881/1000 | Loss: 0.4868
Epoch 882/1000 | Loss: 0.4868
Epoch 883/1000 | Loss: 0.4867
Epoch 884/1000 | Loss: 0.4867
Epoch 885/1000 | Loss: 0.4867
Epoch 886/1000 | Loss: 0.4867
Epoch 887/1000 | Loss: 0.4866
Epoch 888/1000 | Loss: 0.4866
Epoch 889/1000 | Loss: 0.4866
Epoch 890/1000 | Loss: 0.4866
Epoch 891/1000 | Loss: 0.4865
Epoch 892/1000 | Loss: 0.4865
Epoch 893/1000 | Loss: 0.4865
Epoch 894/1000 | Loss: 0.4864
Epoch 895/1000 | Loss: 0.4864
Epoch 896/1000 | Loss: 0.4864
Epoch 897/1000 | Loss: 0.4864
Epoch 898/1000 | Loss: 0.4863
Epoch 899/1000 | Loss: 0.4863
Epoch 900/1000 | Loss: 0.4863
Epoch 901/1000 | Loss: 0.4863
Epoch 902/1000 | Loss: 0.4862
Epoch 903/1000 | Loss: 0.4862
Epoch 904/1000 | Loss: 0.4862
Epoch 905/1000 | Loss: 0.4861
Epoch 906/1000 | Loss: 0.4861
Epoch 907/1000 | Loss: 0.4861
Epoch 908/1000 | Loss: 0.4861
Epoch 909/1000 | Loss: 0.4860
Epoch 910/1000 | Loss: 0.4860
Epoch 911/1000 | Loss: 0.4860
Epoch 912/1000 | Loss: 0.4860
Epoch 913/1000 | Loss: 0.4859
Epoch 914/1000 | Loss: 0.4859
Epoch 915/1000 | Loss: 0.4859
Epoch 916/1000 | Loss: 0.4859
Epoch 917/1000 | Loss: 0.4858
Epoch 918/1000 | Loss: 0.4858
Epoch 919/1000 | Loss: 0.4858
Epoch 920/1000 | Loss: 0.4858
Epoch 921/1000 | Loss: 0.4857
Epoch 922/1000 | Loss: 0.4857
Epoch 923/1000 | Loss: 0.4857
Epoch 924/1000 | Loss: 0.4857
Epoch 925/1000 | Loss: 0.4856
Epoch 926/1000 | Loss: 0.4856
Epoch 927/1000 | Loss: 0.4856
Epoch 928/1000 | Loss: 0.4856
Epoch 929/1000 | Loss: 0.4855
Epoch 930/1000 | Loss: 0.4855
Epoch 931/1000 | Loss: 0.4855
Epoch 932/1000 | Loss: 0.4855
Epoch 933/1000 | Loss: 0.4854
Epoch 934/1000 | Loss: 0.4854
Epoch 935/1000 | Loss: 0.4854
Epoch 936/1000 | Loss: 0.4854
Epoch 937/1000 | Loss: 0.4853
Epoch 938/1000 | Loss: 0.4853
Epoch 939/1000 | Loss: 0.4853
Epoch 940/1000 | Loss: 0.4853
Epoch 941/1000 | Loss: 0.4852
Epoch 942/1000 | Loss: 0.4852
Epoch 943/1000 | Loss: 0.4852
Epoch 944/1000 | Loss: 0.4852
Epoch 945/1000 | Loss: 0.4851
Epoch 946/1000 | Loss: 0.4851
Epoch 947/1000 | Loss: 0.4851
Epoch 948/1000 | Loss: 0.4851
Epoch 949/1000 | Loss: 0.4850
Epoch 950/1000 | Loss: 0.4850
Epoch 951/1000 | Loss: 0.4850
Epoch 952/1000 | Loss: 0.4850
Epoch 953/1000 | Loss: 0.4850
Epoch 954/1000 | Loss: 0.4849
Epoch 955/1000 | Loss: 0.4849
Epoch 956/1000 | Loss: 0.4849
Epoch 957/1000 | Loss: 0.4849
Epoch 958/1000 | Loss: 0.4848
Epoch 959/1000 | Loss: 0.4848
Epoch 960/1000 | Loss: 0.4848
Epoch 961/1000 | Loss: 0.4848
Epoch 962/1000 | Loss: 0.4847
Epoch 963/1000 | Loss: 0.4847
Epoch 964/1000 | Loss: 0.4847
Epoch 965/1000 | Loss: 0.4847
Epoch 966/1000 | Loss: 0.4846
Epoch 967/1000 | Loss: 0.4846
Epoch 968/1000 | Loss: 0.4846
Epoch 969/1000 | Loss: 0.4846
Epoch 970/1000 | Loss: 0.4846
Epoch 971/1000 | Loss: 0.4845
Epoch 972/1000 | Loss: 0.4845
Epoch 973/1000 | Loss: 0.4845
Epoch 974/1000 | Loss: 0.4845
Epoch 975/1000 | Loss: 0.4844
Epoch 976/1000 | Loss: 0.4844
Epoch 977/1000 | Loss: 0.4844
Epoch 978/1000 | Loss: 0.4844
Epoch 979/1000 | Loss: 0.4844
Epoch 980/1000 | Loss: 0.4843
Epoch 981/1000 | Loss: 0.4843
Epoch 982/1000 | Loss: 0.4843
Epoch 983/1000 | Loss: 0.4843
Epoch 984/1000 | Loss: 0.4842
Epoch 985/1000 | Loss: 0.4842
Epoch 986/1000 | Loss: 0.4842
Epoch 987/1000 | Loss: 0.4842
Epoch 988/1000 | Loss: 0.4842
Epoch 989/1000 | Loss: 0.4841
Epoch 990/1000 | Loss: 0.4841
Epoch 991/1000 | Loss: 0.4841
Epoch 992/1000 | Loss: 0.4841
Epoch 993/1000 | Loss: 0.4841
Epoch 994/1000 | Loss: 0.4840
Epoch 995/1000 | Loss: 0.4840
Epoch 996/1000 | Loss: 0.4840
Epoch 997/1000 | Loss: 0.4840
Epoch 998/1000 | Loss: 0.4839
Epoch 999/1000 | Loss: 0.4839
Epoch 1000/1000 | Loss: 0.4839
Prediction (after training) tensor([-0.2941,  0.4874,  0.1803, -0.2929,  0.0000,  0.0015, -0.5312, -0.0333]) : 0.4202234447002411
accuracy :  76.54808959156784
