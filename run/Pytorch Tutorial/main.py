"""
    Intro to Pytorch: https://pytorch.org/tutorials/beginner/blitz/tensor_tutorial.html#sphx-glr-beginner-blitz-tensor-tutorial-py
    Dec 22

    torch.add
    torch.rand
    "matrix".view == reshape
    torch.ones
    convert numpy array into torch tensor: torch.from_numpy("array")

"""
from __future__ import print_function
import torch
import numpy
import torchvision

def main():
    # # Create a tensor
    # x = torch.rand(5,3)
    # y = torch.rand(5,3)
    #
    # a = torch.add(x,y)
    # print(a)
    # a = a.view(15)
    # print(a)
    # print(numpy.shape(a))

    # Convert the numpy array into torch tensor
    a = numpy.ones(5)
    print(f"Numpy array is {a}")
    a = torch.from_numpy(a)
    print(f"The tensor is {a}")


if __name__ == "__main__":
    main()