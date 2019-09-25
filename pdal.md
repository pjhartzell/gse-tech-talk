## 1. Installing PDAL
* Create a new environment: `conda create -n pdal Python=3`
* Install PDAL's Python extension: `conda install -c conda-forge python-pdal`
  * Note that this also installs PDAL as a standalone application
  * Test if the PDAL application installed successfully by typing `pdal` at the prompt.
* Look [here](https://pdal.io/apps/index.html) for more information.

## 2. Using the PDAL command line application
* Example: Get LAS file information
  * `pdal info sample.las`
  * `pdal info sample.las --metadata`
* Example: Convert a LAS file to a text file
  * `pdal translate sample.las sample.txt`
* Example: Take advantage of non-command line PDAL functionality with a **pipeline**
  * A **pipeline** is just a JSON file that *sequentially* specifies an input file, data modification, and an output file.
  * Here is an example that reads in a LAS file, computes the density of points within a radius for each point, and saves the resulting point cloud, including the new density measure, to a CSV format text file:
  ```json
  [
      {
          "type":"readers.las",
          "filename":"sample.las"
      },
      {
          "type":"filters.radialdensity",
          "radius":5
      },
      {
          "type":"writers.text",
          "filename":"radial_density.txt"
      }
  ]
  ```
    * Run `pdal pipeline pipeline_file.json` to execute the example pipeline.
    * Check out the [PDAL website](https://pdal.io/index.html) for more information and examples.
  
## 3. Using PDAL in a Python script or function
### Typical Use Case #1: Running a pipeline
* Sometimes we want to run a pipeline from within Python.
* Here is a simple example that runs the same pipeline as above. Note that we set some of the pipeline values using Python variables:
```Python
import pdal
import json

radius = 5
outfilename = 'radial_density.txt'
json_array = [
    {
        "type":"readers.las",
        "filename":"sample.las"
    },
    {
        "type":"filters.radialdensity",
        "radius":radius
    },
    {
        "type":"writers.text",
        "filename":outfilename
    }
]
pipeline = pdal.Pipeline(json.dumps(json_array))
pipeline.validate()
pipeline.execute()
```

### Typical Use Case #2: Import lidar data to Python variables
* Often what we really want is to just get the lidar points into Python so we can do awesome things with them.
* Still requires a pipeline, but we access the data fields (PDAL calls them *Dimensions*) from the PDAL pipeline object we create:
```Python
import pdal

reader = """
[
    {
        "type":"readers.las",
        "filename":"sample.las"
    }
]"""

pipeline = pdal.Pipeline(reader)
pipeline.validate()
pipeline.execute()
arrays = pipeline.arrays
view = arrays[0]
X = view['X']
Y = view['Y']
Z = view['Z']
I = view['Intensity']

# print some points to test it worked
for i in range(100):
    print('X = {}, Y = {}, Z = {}, I = {}'.format(X[i], Y[i], Z[i], I[i]))
```
* We can also use a PDAL pipeline in Python to save points to a file. Below is an extension of the example above:
```
import pdal
import numpy as np

reader = """
[
    {
        "type":"readers.las",
        "filename":"sample.las"
    }
]"""
pipeline = pdal.Pipeline(reader)
pipeline.validate()
pipeline.execute()
arrays = pipeline.arrays
view = arrays[0]
X = view['X']
Y = view['Y']
Z = view['Z']
I = view['Intensity']

# shift all the points by 100 meters
for i in range(len(X)):
    X[i] += 100

# create a new numpy structured array for output
records = []
for i in range(len(X)):
    records.append((X[i], Y[i], Z[i], I[i])) # we are creating a list of tuples
structured_array = np.array([records], dtype=[('X',np.float), ('Y',np.float), ('Z',np.float), ('Intensity',np.uint16)])

# write the shifted points to a new text file
writer = """
[
    {
        "type":"writers.text",
        "filename":"sample_shifted.txt"
    }
]"""
pipeline = pdal.Pipeline(json = writer, arrays = [structured_array,])
pipeline.validate()
pipeline.execute()
```
