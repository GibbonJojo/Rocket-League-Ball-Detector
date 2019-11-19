# RL Ball Detector
Using OpenCV2, this little piece of code is for detecting the ball in Rocket League.

Written to play around with OpenCV a little bit.

Usually works as intended:
![](figures/python_2019-11-19_09-29-30.png?raw=true)

But due to a lot going on in the screen, (see right image) the detection is still flawed. Parameter tuning didn't get me the desired result so far, just because either too many edges get detected and therefore to many circles, or not enough edges get detected and no circles appear.

![](figures/python_2019-11-19_09-32-14.png?raw=true)
