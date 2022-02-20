#5
linear.eval()
with torch.no_grad():
    correct = 0
    total = 0
    for i, (imgs, labels) in enumerate(test_loader):
        imgs, labels = imgs.to(device), labels.to(device)
        imgs = imgs.view(-1, 28*28)
        outputs = linear(imgs)
        _, argmax = torch.max(outputs, 1) #max를 통해 최종 출력이 가장 높은 class 선택
        correct += (labels == argmax).sum().item()

        print('Test accuracy for {} images: {:.2f}%'.format(total, correct / total*100))