
import base64
image = open('repriles.mp4', 'rb')
image_read = image.read()
image_64_encode = base64.encodestring(image_read)
print image_64_encode


image_64_decode = base64.decodestring(image_64_encode) 
image_result = open('rep_decode.mp4', 'wb') # create a writable image and write the decoding result
image_result.write(image_64_decode)
