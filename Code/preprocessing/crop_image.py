import os
import cv2

# Function to rename multiple files

src_path = '/content/drive/MyDrive/stylegan2DS/openlogo/'
dst_path = '/content/drive/MyDrive/stylegan2DS/openlogo128/'
count = 0
def main():
  for _, dirpath in enumerate(os.listdir(src_path)):
    for _, filename in enumerate(os.listdir(src_path+dirpath)):
        img = cv2.imread(src_path+dirpath + "/" + filename)
        resize = cv2.resize(img, (128, 128))
        cv2.imwrite(dst_path + "/" + filename, resize)
        count+=1
        print(count)

# Driver Code
if __name__ == '__main__':
    # Calling main() function
    main()
