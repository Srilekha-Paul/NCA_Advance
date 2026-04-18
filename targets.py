     import numpy as np

def heart(size=64):
    img = np.zeros((size,size,4), dtype=np.float32)

    for y in range(size):
        for x in range(size):
            X=(x-size/2)/(size/2)
            Y=(y-size/2)/(size/2)

            if (X**2 + Y**2 -0.3)**3 - X**2*Y**3 <0:
                img[y,x,:3]=[1,0,0]
                img[y,x,3]=1

    return img