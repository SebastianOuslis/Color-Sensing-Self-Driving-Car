# Color-Sensing-Self-Driving-Car
Created By Sebastian Elo Ouslis
Created on 2017/03/13
The code that can be found in this repository was written in python and was tested using the raspberry pi 3.
A large amount of the array functionality came from two libraries, Open CV (specifically open cv2) and Numpy.
Open CV was used to convert the raw data from the camera into an array of pixels and eventually create a histogram from those pixels.
Numpy was used to create arrays to hold this data.

#Thanks:
Thank you to Adrian Rosebrock and his website PyImageSearch for his resources in image processing and machine learning. His explanations and tutorials were integral in understanding how the image processing worked and how to implement it. Along with this, he had tutorials on how to install the libraries required to do the image processing.

#Image Processing and How the Color Recognition Works:
The car uses a raspberry pi and the camera attachment. At a certain time interval, the car takes a picture using the camera. It then changes this picture into a pixel array.
Color sensing is effective because the pictures can be analysed by looking at the intensity of each color in each pixel.
From there, the array from the picture is very large. To fix this issue, I take the middle of the picture by splitting it up. This focuses the view of the picture into the center of the field of vision.
I then create a histogram of the colors and normalize that histogram. It can be normalized with any value, I chose 3 because I had three colors and three intensities of color.
Finally, using the values taken from the histogram, the number of very bright pixels, medium pixels, and low pixels or each color, a decision is made about the color of the picture.
The values set for finding each color have been found through much trial and error. These values are the most accurate in a bright environment with strong colors. It is very difficult to get the blue color to be detected and for that reason, it is not used as a signal for anything.
If the environment is relatively bright and has a variety of colors, the car will most likely see grey and will move forwards. If the camera is covered, it will see black and stop or is a very black object is put in the view of the camera.
Green and Red are used as signals for turning because they are easily detected by the camera.
Please test more colors and contact me if you have found better calibration for the color sensing.

#Motor Driver Class:
The current code is created for a car with two wheels that can only turn or go forwards. This can easily be changed to work with a full motor driver with reverse functionality and two wheels. The motor driver class
was created to use with a proper motor driver and two wheels. It is capable of moving forwards, backwards, and turn either direction
The code for the self driving car implements the motor class written by me. I did not have a full motor driver and instead created one from scratch that was not capable of reversing the wheels.
For this reason, I have only used a quarter of the driver. Along with this, the driver was created to function for a motor driver created from mosfets. 
Please read the section below before using the motor driver class because it has been created with the use of mosfets in mind 
The motor driver class works for a motor driver that is as follows. 

                     Input 1                   Input 2
                        |                         |
      Power -------  P MOSFET  --------------- N MOSFET ------- Ground
                                     |
                                     |
                                   Motor
                                     |
                       Input 3       |             Input 4
                         |           |               |
       Ground ------  N MOSFET ----------------- P MOSFET ------ Power


In this diagram, the top left P Mosfet is connected to both the top right N Mosfet and one side of the motor. The Bottom left N Mosfet is connected to the bottom right
P Mosfet and the other side of the motor. When the P mosfets are given a low input signal, they open up and allow the current to flow through. For this motor driver
all the P Mosfets are connected to power and would be supplying power to the Motor. When the N Mosfet is given a High signal, it allows the current to flow through it and to ground.
An advantage to using a motor driver class is that it guarantees that the battery controlling the motor will not short because if both the N and P on a row was turned on at the same time, it will short your battery.
Though the diagram above could be drawn with inputs 1 and 2 the same and inputs 3 and 4 the same, the class is written with separate outputs to make sure there is no chance of a short circuit in case something is wired incorrectly.
The motor driver class allows for easy functionality and motor control with two wheels. It has the ability to control two separate motors using its outputs and the circuit above.

#Kickback Protection:
In order to protect my raspberry pi and transistors from the kickback from the motors, I had to create a circuit that would control where the current would go.
The circuit is the same for each motor. The whole circuit for the car is shown on a fritzing diagram attached and will be drawn out (apologies for the bad drawing).

#Contact Information:
If you have any questions, please feel free to email me at sebastian.elo.ouslis@gmail.com for any issues or questions. If you need any help with any projects, please contact me.
If this project has helped you with anything you are doing, I would appreciate an email outlining what you did so that I can see what amazing things people have accomplished.
Feel free to take, modify or use any of my code for educational purposes or for hobby projects.
