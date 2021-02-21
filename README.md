# EdgeDepth
Some code blocks that help you to test Depth Camera(as well as vocie recognition) on Edge devices.
Edge devices include NVIDIA Jetson Nano and Raspberry pi 4
Depth camera includes Intel RealSense D435i.

## Install RealSense SDK
It is necessary to install Relasense SDK to use Depth Camera.This page is helpful to install RealsenseSDK on RPI4
https://github.com/acrobotic/Ai_Demos_RPi/wiki/Raspberry-Pi-4-and-Intel-RealSense-D435

## Voice Recognition
Simple voice recognition code is also included in this repository to trigger depth camera with vocie command.
It is construced  in a way that the user can wake up the device with a specific word, and command.
For example, wake up the deivce by calling it "kd" and command "Take snapshot" to take a depth image of surroundings.

