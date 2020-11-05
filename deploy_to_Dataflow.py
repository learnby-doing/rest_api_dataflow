import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions, StandardOptions

import os
os.environ["GOOGLE_APPLICATION_CRENDENTIALS"] = "C:\\Users\\ASHISH\\Desktop\\GCP\\dhamu-gcp-learn.json"


def pipeline(input_file, output_file, pipline_args):
    
    import apache_beam as beam
    from apache_beam.options.pipeline_options import PipelineOptions
    import os
    os.environ["GOOGLE_APPLICATION_CRENDENTIALS"] = "C:\\Users\\ASHISH\\Desktop\\GCP\\dhamu-gcp-learn.json"
    options = PipelineOptions(pipline_args)
    p = beam.Pipeline(options = options)
    print(os.environ['GOOGLE_APPLICATION_CREDENTIALS'])

    attendatn_count = (
        p
        | 'Read from text' >> beam.io.ReadFromText(input_file)
        | 'Spilt Row' >> beam.Map(lambda elem: elem.split(","))
        | 'Write to Text' >> beam.io.WriteToText(output_file,"",shard_name_template="")
    )
    return p

from flask import request,Flask
import json
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/",methods=['GET',"POST"])
def hello_world():
    if request.method == "POST":
        data = json.loads(request.get_data().decode("utf8"))
        
        print(data)
        print(f"input file: {data.get('input')}")
        print(f"output file: {data.get('output')}")
        input_file = data.get('input')
        output_file = data.get('output')
        pipeline_args = [f"--{key}={data.get('pipeline_args')[key]}" for key in data.get('pipeline_args')]
        print(pipeline_args)
        p = pipeline(input_file,output_file,pipeline_args)
        p.run()
    
    
    return "hello world"

app.run()

