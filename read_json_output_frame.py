import json
class Config:
    def __init__(self, config):
        self.config = config
        self.source_type = config['source_type']
        self.camera_name = config['camera_name']
        self.video_file_name = config['video_file_name']
        self.total_image_frames = config['total_image_frames']

        self.input_tensor_height = config['input_tensor_height']
        self.input_tensor_width = config['input_tensor_width']
        self.output_tensor_height = config['output_tensor_height']
        self.output_tensor_width = config['output_tensor_width']
        
        self.traffic_counting_line = config['traffic_counting']
        self.bike_counting_line = config['bike_counting']
        self.pedestrian_counting_line = config['pedestrian_counting']

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

if __name__ == "__main__":
    file_path = 'curb_management/json_output_schema/sj_curb_output_sample_frame.json'
    json_data = read_json_file(file_path)

    config = json_data['config']
    output = json_data['output']

    co = Config(config)
