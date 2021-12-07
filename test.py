import torch
a = torch.zeros((128,256,100,100), dtype=torch.uint8)
for i in range(32):
    a[:,i,:,:] = i

a = torch.moveaxis(a,1,0)
a[1,:]

lol = (a > 2).sum((1,2,3))