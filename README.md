# About this Repository:

<b>Objectives Achieved:</b>
1. Successfully Lip Synced the desired video with Visual and Audio Quality.
2. Unlike the original Wav2Lip model that needs a face in all the video frames, the model developed can be applied without errors to any Video(with or without a face in video frames)
3. The developed model can handle Longer Videos (Over 1 min long) which the original Wav2Lip model can't.
4. Improved the inference model of the Wav2Lip.
<br>
<b>Challenges:</b><br>
1. Wav2Lip with GAN doesn't provide good lipsync for longer videos, videos with any head movement, and high-resolution videos.<br>
2. Wav2Lip also doesn't have a mechanism to make a distinction between the target speaker and other faces that appears in the video.<br>
3. The problems with longer and high-resolution videos, videos with some frames without a face have been solved in the notebook, however, solving challenge 2 would require deeper changes to the Wav2Lip model.<br>
4. Long runtimes for longer videos.<br>
<br><br>
<b>NOTE:</b><br>
1. For 10 minutes or longer Youtube Videos took over 5-7 minutes to load and clip the part necessary for lip-sync in the notebook.<br>
2. Therefore for the default link attached in the Colab Notebook, I have clipped the necessary (to be lipsync) portion which is 1 min 25 seconds long, and uploaded it on youtube, from where we could load the video more easily.<br>
3. It has a watermark of the Video Editing tool used to clip the 10 min video with.<br>


# For More info about Wav2Lip scroll below:
# **Wav2Lip**: *Accurately Lip-syncing Videos In The Wild*
License and Citation
----------
This repository can only be used for personal/research/non-commercial purposes. However, for commercial requests, please contact us directly at radrabha.m@research.iiit.ac.in or prajwal.k@research.iiit.ac.in. We have an HD model trained on a dataset allowing commercial usage. The size of the generated face will be 192 x 288 in our new model. Please cite the following paper if you use this repository:
```
@inproceedings{10.1145/3394171.3413532,
author = {Prajwal, K R and Mukhopadhyay, Rudrabha and Namboodiri, Vinay P. and Jawahar, C.V.},
title = {A Lip Sync Expert Is All You Need for Speech to Lip Generation In the Wild},
year = {2020},
isbn = {9781450379885},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/3394171.3413532},
doi = {10.1145/3394171.3413532},
booktitle = {Proceedings of the 28th ACM International Conference on Multimedia},
pages = {484–492},
numpages = {9},
keywords = {lip sync, talking face generation, video generation},
location = {Seattle, WA, USA},
series = {MM '20}
}
```

