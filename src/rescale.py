import cv2 as cv

def rescale_frame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# Resize images
# large_cat_img = cv.imread("../resources/Photos/cat_large.jpg")
# smaller_cat_img = rescale_frame(large_cat_img, 0.1)
# cv.imshow('Cat', smaller_cat_img)
# cv.waitKey(0)


# Resize video
# capture = cv.VideoCapture("../resources/Videos/dog.mp4")
# while True:
#     isTrue, frame = capture.read()
#     resized_frame = rescale_frame(frame)

#     cv.imshow('Video', resized_frame)

#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()


# Live video
def change_res(width, height):
    capture.set(3,width)
    capture.set(4,height)