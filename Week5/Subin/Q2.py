#2
device = torch.device('cuda' if torch.cuda_is_available() else 'cpu')
linear = torch.nn.Linear(784, 10, bias=True).to(device)
torch.nn.init.normal_(linear.weight)