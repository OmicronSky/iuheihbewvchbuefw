import audio

# read the files from the microbit filesystem
def read_frame(f_list, frame):
    for file in f_list:
        ln = file.readinto(frame)
        while ln:
            yield frame
            ln = file.readinto(frame)

# craete a function to open and play each file in turn
def play_file(f):
    with open(f + "-01.raw", "rb") as file1, \
         open(f + "-02.raw", "rb") as file2, \
         open(f + "-03.raw", "rb") as file3, \
         open(f + "-04.raw", "rb") as file4:
        f_list = [file1, file2, file3, file4]
        audio.play(read_frame(f_list, frame), wait=True)


# Allocate memory outside the interrupt
frame = audio.AudioFrame()
ln = -1
file = 1

# play the files
play_file("robot")