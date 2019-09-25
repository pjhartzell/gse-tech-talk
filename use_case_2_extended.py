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
