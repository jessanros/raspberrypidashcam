# Raspberry Pi Touchscreen Dashcam

### Description
This project includes software that allows a Raspberry Pi with a touchscreen to serve as a dashcam in the background. The software will record and  place a red blinking button at the top right corner of the screen. If pressed, the user can see what's being recorded. A semi-transparent floating screen will show you a preview of what's being recorded on top of any other Raspberry application.

With the help of Android Auto, the Raspberry Pi is also capable of displaying GPS information, music, and SMS/Call notifications without the need of picking up your phone. All while recording the front of the car and keeping the videos for 30 days.

Videos are saved as raw h264 files, and can be easily converted to .mp4/.mkv. Videos older than a given time period will be automatically deleted.

Recently added a minimalistic video player, but that is not the real intent of this project.

I recommend this software use with Android Auto! I used https://github.com/f1xpl/openauto, and will be making a writeup about the installation!

<a href='https://photos.google.com/share/AF1QipPFi9j003T0m7irMuteYjvDvm_oBUNlAvVtjbGcAWuArn2QXhshB2xr4euxRKBMQQ?key=ZmVuNE1qUlkyalIzUGU1VVd6S3lXZjE5Wks1bEZn&source=ctrlq.org'><img src='https://lh3.googleusercontent.com/wF4T_DoXvKUIKpAUVbDLOjs09R0fuy2OzPC2XBlzOrXRTpmnNsWubkGKHHD_PZsEpMzTBTluHjMZ77C5ctkzbRRqdRjJG9FRn8fGHGn2nO92by5t6_-DXAIBfQwVV7t65Roe9p5T_zw=w2400' /></a>

<a href='https://photos.google.com/share/AF1QipMTfZOLtocCwxj2pG3h_KUuP54pWVTIlhc7O90gFnWEnOkBINuojSUpcmEmR93MXA?key=ZlJITV9tTE9TRWVzc3dIYmF6d0FEUWM3NGsxRDh3&source=ctrlq.org'><img src='https://lh3.googleusercontent.com/mw_xq_A3Pch9CyPguLtXWnoQo2v_NUucVgW5Ffk-tL5WZjKLn2R3TyXoHvupju91wfnh7M73Gdd_vDFco51JPHVpPWrsO2FbUB29jS5RoHipaINYk0oanOVm8JK5Y-ejb3D6e8Nztos=w2400' /></a>

<a href='https://photos.google.com/share/AF1QipOqDSTzNm5KkKaOuJMfBOVGYqaM79hTZL98cogSj2IgFoDZJuNjY-nyC3ljMbUuLQ?key=bXFrWUs4M1k2WUYtNnQ3dUpidV9QanVydUhBV3Z3&source=ctrlq.org'><img src='https://lh3.googleusercontent.com/UFRQfdzPm5dzyUtZhvplbLHcfKP8CycYyFWCFtF0OaxHRz-_fPRjc5p4yQS9-Ne-10ngHP419jawTsuOuDPtVb4war_hFmZ8bphD3Hkx7I7s0VmULiqODEWAV3F0fSlfqqBXkP-xcy8=w1200' /></a>

<a href='https://photos.google.com/share/AF1QipM3Z44PGguVld_x6mKBGurcPsgTw-sTk0jpwqaAGTRP3a5TnSeOZxJiJDg89D0okA?key=NHJtd1RTUjVoLXBTT3h6VUdxVnk0ZW8wcEQwU1l3&source=ctrlq.org'><img src='https://lh3.googleusercontent.com/Laa8AIhcpYkiJBHh6dboFJIzoi4DRr0bFzOy_f8mSErmxbiQmXpbn2p7sn4V9a5MyaX4S7WlXdCDN0FTvzOQlAKiGqYcbK_EpNaoG30XmsRZxRTZewpJcUnnXyGUD133Ff-UWcia0Ac=w2400' /></a>

<a href='https://photos.google.com/share/AF1QipOKuo-xBXmD069m72y19DFg99uLVzjrJV2hxzNiq1ToRyeqMfpJjhL_1WDggZexBA?key=RHVibkRRbEt0X0g2MURvMS1nT1djUHNtNVc3YVln&source=ctrlq.org'><img src='https://lh3.googleusercontent.com/Ry1MkTdrAP-N-mXlw1x5yiPkDlhpXFhgWlqouy96iSIuWjFR5RGSkAYjAXRadEcMZxG0Mdq8-0YBK2u2Ckzh1rNVJFmIPWq6oIYk_mLoQGLGN6sWDRCP4t62WIcbOS7zt3Z4QbtrHyA=w2400' /></a>

Watch a demo of it working here!

[![See recording samples!](https://img.youtube.com/vi/3dCEsQB9DQs/0.jpg)](https://www.youtube.com/watch?v=3dCEsQB9DQs)

[![See demo video](https://img.youtube.com/vi/fsGw8uXxl4c/0.jpg)](https://www.youtube.com/watch?v=fsGw8uXxl4c)
