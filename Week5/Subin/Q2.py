<<<<<<< HEAD
#2
device = torch.device('cuda' if torch.cuda_is_available() else 'cpu')
linear = torch.nn.Linear(784, 10, bias=True).to(device)
=======
#2
device = torch.device('cuda' if torch.cuda_is_available() else 'cpu')
linear = torch.nn.Linear(784, 10, bias=True).to(device)
>>>>>>> 1cd0b0ddf18224d14fbbee1430d43df0883cff73
torch.nn.init.normal_(linear.weight)