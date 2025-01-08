![img.png](img.png)

Файл состоит из байтов 2 типоа: 255 и 0. Можно собрать из него
QR-код. 

```python
from numpy import genfromtxt
import matplotlib
from matplotlib import pyplot
from matplotlib.image import imread


my_data = genfromtxt('ste.csv', delimiter=',')
matplotlib.image.imsave('output.png', my_data, cmap='gray')
image_1 = imread('output.png')
pyplot.imshow(image_1)
pyplot.show()
```
А вот и он:

![img_1.png](img_1.png)

По ссылке, зашитой в нём, находим флаг.
flag{that_will_be_five_dollars}