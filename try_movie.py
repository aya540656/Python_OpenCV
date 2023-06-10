# %%
import cv2

# %%
data = cv2.VideoCapture('./sample.mp4')

# %%
type(data)

# %%
data.isOpened()

# %%
while True:
    ret, frame = data.read()
    if ret:
        cv2.imshow('sample data', frame)
        cv2.waitKey(1)
        key = cv2.waitKey(1)
        if key & 0x00FF  == ord('q'):
            break
    else:
        data.set(cv2.CAP_PROP_POS_FRAMES, 0)

cv2.destroyWindow('sample data')


# %%



