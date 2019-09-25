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