### image mosaicing
- presently we are using opencv_contrib

- this is done in 3 parts

	- homography 
	this is done by find the matching features between images

	- warping 
	planar surface is taken for warping and the images are modified with their respective homography matrix

	- blending
	the images are added to get the final image. Along with this we will try to do multiband image smoothning is done to ensure clear output.
