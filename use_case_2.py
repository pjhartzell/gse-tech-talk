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