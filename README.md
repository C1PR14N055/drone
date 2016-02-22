# drone
Just pieces as of now

Trying to build a drone ^_^

###Usefull cmds for now

#change SD partition table
sudo fdisk /dev/mmcblk0

#format SD as FAT32
sudo mkfs.vfat -F 32 /dev/mmcblk0

#write image (unmount SD first)
sudo dd bs=4M if=2015-11-21-raspbian-jessie.img of=/dev/mmcblk0

#track img writing progress
sudo pkill -USR1 -n -x dd

#fix mouse lag
add usbhid.mousepoll=0
to /boot/cmdline.txt

#ssh into pi
ssh pi@192.168.1.87

#scp, copy files from one to another (while not ssh-ing)
scp pi@192.168.1.87:/Desktop/video.h264 /Desktop/video.h264

#shutdown at a certain tine
shutdown -h 21:19

#record video 5 seconds
raspivid -o video.h264 -t 5000

#mplayer and nc.traditional streaming
#on pc
mkfifo fifo.264
nc.traditional -l -p 5000 > fifo.264 | mplayer -fps 30 fifo.264 -cache 1024
#on pi
cat fifo.264 | nc.traditional 192.168.1.143 5000 & /opt/vc/bin/raspivid -o fifo.264 -t 10000000 -b 2000000

#settup uv4l
http://www.linux-projects.org/modules/sections/index.php?op=viewarticle&artid=14
http://www.instructables.com/id/Raspberry-Pi-Video-Streaming/?ALLSTEPS

#run uv4l
sudo uv4l -nopreview --auto-video_nr --vflip yes --driver raspicam --encoding mjpeg --width 640 --height 480 --framerate 60 --server-option '--port=9090' --server-option '--max-queued-connections=30' --server-option '--max-streams=5' --server-option '--max-threads=29'

#stop uv4l
sudo pkill uv4l

#stop uv4l driver
sudo service uv4l_raspicam stop
