"""
    Pytorch Tutorials on First NN
    https://pytorch.org/tutorials/beginner/blitz/autograd_tutorial.html
"""
import torch

def auto_dif():
    # Create a tensor and track computation with it
    x = torch.ones(2,2, requires_grad=True)
    print(x)
    y = x + 2 # auto make 2 as the same for mat
    print(y.grad_fn)

    z = y*y*3
    out = z.mean()
    print(z, out)

if __name__ == "__main__":
    auto_dif()