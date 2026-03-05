import qrcode
import matplotlib.pyplot as plt
import sys

if len(sys.argv) > 1:
    data = " ".join(sys.argv[1:])
else:
    data = input("Enter text for QR code: ")

qr = qrcode.make(data)
plt.figure(facecolor='Grey')

#colors = ['#FFFFFF', '#00008B']  # [background, foreground] - white & dark blue
#custom_cmap = mcolors.ListedColormap(colors) #cmap='Greens'
plt.imshow(qr, cmap='Blues', interpolation='nearest'); plt.axis('off'); plt.show()
#qr.show()  # Opens in default image viewer