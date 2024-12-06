import os
import json
from jsonschema import validate, Draft7Validator, RefResolver

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

if __name__ == "__main__":

    base_path = os.path.dirname(os.path.abspath(__file__))
    schema_path = os.path.join(base_path, 'schema/output_main_schema.json')
    sample_path = os.path.join(base_path, 'sample/event_output_sample.json')

    main_schema = read_json_file(schema_path)
    sample = read_json_file(sample_path)
    
    try:
        # validate(instance=sample, schema=main_schema)
        resolver = RefResolver(base_uri="file:///C:/Users/3000095175/Documents/codes/eval-ai-models/", referrer=True)
        Draft7Validator(main_schema, resolver=resolver).validate(sample)
        print("The JSON sample is valid")
    except Exception as e:
        print("The JSON sample is invalid:", e)
