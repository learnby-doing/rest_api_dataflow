from flask import request,Flask
import json
from deploy_to_Dataflow import pipeline
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
    # print(f"request:{request}")
    
    return "hello world"

app.run()