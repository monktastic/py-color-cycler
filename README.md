
Takes an image and creates a color-cycled mp4 accompanied by the supplied music.

## Step 1: Create images

Run the python code to turn the given image into 100 color cycled jpegs. First you'll need to pip install a few packages:

- pip install opencv-python
- pip install numpy
- pip install Pillow
- pip3 install progressbar2

Then run:
`$ python color_cycle.py sky-diamonds.jpg`

## Step 2: Turn images into mp4

`$ ffmpeg -r 10 -i sky-diamonds-%02d.jpg -vcodec mpeg4 -y movie.mp4`

(r is framerate in FPS)

## Step 3: Create output mp4

`$ ffmpeg -loop 1 -t 439 -framerate 10 -i sky-diamonds-%02d.jpg -i song.mp3 -c copy -c:v libx264 -map 0:v:0 -map 1:a:0 output.mp4`

t is the duration of the song in seconds. The "-c:v libx264" option makes it take longer but creates a much smaller output

## Step 4: Delete intermediate images

`$ rm sky-diamonds-%02d.jpg`

## Optional: Create an animated gif

Install imagemagick (brew install imagemagick)

`convert -delay 0 -loop 0 *-??.jpg sky-diamonds.gif`


## References

https://stackoverflow.com/questions/44947505/how-to-make-a-movie-out-of-images-in-python
https://video.stackexchange.com/questions/12905/repeat-loop-input-video-with-ffmpeg
https://superuser.com/questions/590201/add-audio-to-video-using-ffmpeg

