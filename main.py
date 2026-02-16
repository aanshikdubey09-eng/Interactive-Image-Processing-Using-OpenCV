# Interactive Image Processing Using OpenCV

import cv2
import numpy as np


def load_image():
    path = input("Enter image path: ")
    img = cv2.imread(path)
    if img is None:
        print("Could not load image. Check the path.")
        return None
    return img


def to_grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


def apply_blur(img):
    choice = input("Choose blur type (1-Gaussian, 2-Median): ")
    if choice == '1':
        return cv2.GaussianBlur(img, (5, 5), 0)
    elif choice == '2':
        return cv2.medianBlur(img, 5)
    else:
        print("Invalid choice.")
        return img


def detect_edges(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (7, 7), 0)

    edges = cv2.Canny(blur, 50, 150)

    return edges


def threshold_image(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    print("1 - Binary")
    print("2 - Binary Inverse")
    choice = input("Select: ")

    if choice == '1':
        _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    elif choice == '2':
        _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
    else:
        print("Invalid choice.")
        return gray

    return thresh


def detect_contours(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    thresh = cv2.adaptiveThreshold(
        blur,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY_INV,
        11,
        2
    )

    contours, _ = cv2.findContours(
        thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    output = img.copy()
    count = 0

    for cnt in contours:
        area = cv2.contourArea(cnt)

        if area > 4000:   # Adjust if needed
            cv2.drawContours(output, [cnt], -1, (0, 255, 0), 2)
            count += 1

    print("Number of objects detected:", count)
    return output

def color_detection(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    print("Choose color:")
    print("1 - Green")
    print("2 - Blue")
    print("3 - Yellow")

    choice = input("Select: ")

    if choice == '1':
        lower = np.array([35, 50, 50])
        upper = np.array([85, 255, 255])
    elif choice == '2':
        lower = np.array([90, 50, 50])
        upper = np.array([145, 255, 255])
    elif choice == '3':
        lower = np.array([20, 100, 100])
        upper = np.array([35, 255, 255])
    else:
        print("Invalid choice.")
        return img

    mask = cv2.inRange(hsv, lower, upper)

    contours, _ = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    output = img.copy()

    for cnt in contours:
        if cv2.contourArea(cnt) > 500:
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return output

def resize_image(img):
    scale = float(input("Enter scale factor (e.g., 0.5 or 2): "))
    return cv2.resize(img, None, fx=scale, fy=scale)

def save_image(img):
    name = input("Enter filename to save (e.g., output.jpg): ")
    cv2.imwrite(name, img)
    print("Image saved as", name)

def main():
    img = load_image()
    if img is None:
        return

    current = img.copy()

    while True:
        print("\n---- IMAGE PROCESSING TOOL ----")
        print("1 - Grayscale")
        print("2 - Blur")
        print("3 - Edge Detection")
        print("4 - Threshold")
        print("5 - Contour Detection")
        print("6 - Color Detection")
        print("7 - Resize Image")
        print("8 - Save Image")
        print("0 - Exit")

        choice = input("Select option: ")

        if choice == '1':
            current = to_grayscale(current)
        elif choice == '2':
            current = apply_blur(current)
        elif choice == '3':
            current = detect_edges(current)
        elif choice == '4':
            current = threshold_image(current)
        elif choice == '5':
            current = detect_contours(current)
        elif choice == '6':
            current = color_detection(current)
        elif choice == '7':
            current = resize_image(current)
        elif choice == '8':
            save_image(current)
            continue
        elif choice == '0':
            break
        else:
            print("Invalid option.")
            continue

        #by default image size would be scaled down to 50% for better view
        display_img = cv2.resize(current, None, fx=0.5, fy=0.5)
        cv2.imshow("Result (Resized View)", display_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    print("Program ended.")


if __name__ == "__main__":
    main()
