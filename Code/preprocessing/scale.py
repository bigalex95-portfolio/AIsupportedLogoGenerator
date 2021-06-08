# Pythono3 code to rename multiple
# files in a directory or folder

# importing os module
import os
import cv2

# Function to rename multiple files

src_path = './train/'
dst_path = './train400/'

def main():
    for _, dirpath in enumerate(os.listdir(src_path)):
        for _, filename in enumerate(os.listdir(src_path + dirpath)):
            #print(src_path + dirpath + "/" + filename)
            img = cv2.imread(src_path + dirpath + "/" + filename)
            resize = cv2.resize(img, (400, 400))
            if not os.path.exists(dst_path + dirpath + "/"):
                os.makedirs(dst_path + dirpath + "/")
            print(dst_path + dirpath + "/" + filename)
            cv2.imwrite(dst_path + dirpath + "/" + filename, resize)
            
    cv2.destroyAllWindows()


# Driver Code
if __name__ == '__main__':
    # Calling main() function
    main()
