import qrcode
import matplotlib.pyplot as plt
import sys
import tkinter as tk

def get_clipboard_text():
    """Return clipboard content as string, or None if failed."""
    root = tk.Tk()
    root.withdraw()  # hide the window
    try:
        return root.clipboard_get()
    except tk.TclError:
        return None
    finally:
        root.destroy()

def is_url(text):
    """Return True if text starts with http:// or https://."""
    return text.startswith(('http://', 'https://'))

#clipboard = get_clipboard_text()
#print("clipboard:",clipboard)

if len(sys.argv) > 1:
    data = " ".join(sys.argv[1:])
elif is_url(get_clipboard_text()):
    data = get_clipboard_text()
else:
    data = input("Enter text for QR code: ")

#a,b,c = data.partition("?")

qr = qrcode.make(data.split("?", 1)[0])
plt.figure(facecolor='Grey')

#colors = ['#FFFFFF', '#00008B']  # [background, foreground] - white & dark blue
#custom_cmap = mcolors.ListedColormap(colors) #cmap='Greens'
plt.imshow(qr, cmap='Blues', interpolation='nearest'); plt.axis('off'); plt.show()
#qr.show()  # Opens in default image viewer