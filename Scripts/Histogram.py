from matplotlib import pyplot as plt
import skimage.io
import skimage.color

file = "../Images/test.png"
image = skimage.io.imread(file)

transparency = float(0.4)
plt.xlabel('Intensity Value')
plt.ylabel('Count')

plt.hist(image.ravel(), bins=128, color='grey', alpha=0.5)
plt.hist(image[:, :, 0].ravel(), bins=128, color='red', alpha=transparency)
plt.hist(image[:, :, 1].ravel(), bins=128, color='Green', alpha=transparency)
plt.hist(image[:, :, 2].ravel(), bins=128, color='Blue', alpha=transparency)

plt.legend(['Total', 'Red', 'Green', 'Blue'])
try:
    plt.savefig(f"{file}1.jpg")
except:
    print("Error saving file...")
    print("Passing...")
plt.show()
