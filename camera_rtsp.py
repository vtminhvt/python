import cv2
import numpy as np

def read_rtsp_stream(url):
    # Mở kết nối RTSP
    connection = cv2.VideoCapture(url)
    if not connection.isOpened():
        print("Không thể mở kết nối RTSP")
        return

    # Lặp lại để đọc dữ liệu từ camera
    while True:
        # Đọc một khung hình từ camera
        ret, frame = connection.read()
        if not ret:
            break

        # Xử lý khung hình
        # ...

        # Hiển thị khung hình
        cv2.imshow("Camera", frame)

        # Đợi nhấn phím q để thoát
        key = cv2.waitKey(1)
        if key == ord("q"):
            break

    # Đóng kết nối RTSP
    connection.release()

if __name__ == "__main__":
    # URL của camera
    url = "rtsp://192.168.1.100:554/stream1"

    # Đọc dữ liệu từ camera
    read_rtsp_stream(url)
