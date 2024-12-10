# HFS-Muography

This repository contains a quick and simple exercise of scattering muography based on the Point-Of-Closest approach algorithm. The exercise has been designed to complement this muon tomography lecture at the HSF-VECC workshop in Kolkata 15th-20th December 2024.

1.- Dependencies

The code has been prepared to run in a linux machine using python3, numpy, pandas, pytables and matplotlib libraries. 

2.- Running the code

Please make sure that you add the tools directory to the PYTHONPATH variable. You can do that by simply sourcing setup.sh.

source setup.sh

Then simply run the code by typing:

python runAlgorithm.py --input path_to_the_input_file --output name_of_the_figure

3.- Exercise

3.1 Have a look at the code and run it to become familiar with it.

3.2 Find values for threshold1 and threshold2 that produce the best quality plot. 

3.3 Comment on the following questions:

- Is the quality of the image the same in the three projections? Try to think why. 

- Why the center of the image looks "better" than the sides?

- How would you expect the thresholds to change if we would be looking at a lighter object?

3.4 Focus on the projection XY and implement new plots in which only POCA points in a given Z range are allowed. Once you have that, produce different Z "slices" and visualize the results.




