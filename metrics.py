!pip install opencv-python
import cv2
import numpy as np

def calculate_mse(frame1, frame2):
    return np.mean((frame1 - frame2) ** 2)

def calculate_psnr(frame1, frame2):
    mse = calculate_mse(frame1, frame2)
    max_pixel_value = 255.0
    psnr = 20 * np.log10(max_pixel_value / np.sqrt(mse))
    return psnr

lip_synced_video = cv2.VideoCapture('/content/Wav2Lip/results/result_voice.mp4')
ground_truth_video = cv2.VideoCapture('/content/sample_data/resized_video.mp4')

total_frames = int(lip_synced_video.get(cv2.CAP_PROP_FRAME_COUNT))

mse_values = []
psnr_values = []

for i in range(total_frames):
    ret1, frame1 = lip_synced_video.read()
    ret2, frame2 = ground_truth_video.read()
    
    if not ret1 or not ret2:
        break
    
    # Convert frames to grayscale (if needed)
    frame1_gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    frame2_gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    mse = calculate_mse(frame1_gray, frame2_gray)
    psnr = calculate_psnr(frame1_gray, frame2_gray)

    mse_values.append(mse)
    psnr_values.append(psnr)

lip_synced_video.release()
ground_truth_video.release()

average_mse = np.mean(mse_values)
average_psnr = np.mean(psnr_values)

print("Average MSE:", average_mse)
print("Average PSNR:", average_psnr)
