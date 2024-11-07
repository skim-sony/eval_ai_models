# Descriptions for standardized json output

This readme describes the json output schemas that we standardized for AITRIOS AI model and post-processing algorithms. Currently, we support two use-cases: curb management and traffic counting. 
- frame_output_schema.json: output schema for frame-based output

----

### frame_output_schema.json

#### config
| Field Name            | Required  | Data Type | Description |
|-----------------------|-----------|-----------|-------------|
| source_type           |   Y       | string    | The timestamp of the frame in ISO 8601 format |
| camera_id             |   Y       | integer   | Camera id |
| video_file_name       |   N       | string    | Video file name; leave as 'null' if it's online processing |
| total_image_frames    |   N       | integer   | The number of total images for processing; leave as -1 if it's online processing |
| input_tensor_height   |   Y       | integer   | Input tensor size (height) |
| input_tensor_width    |   Y       | integer   | Input tensor size (width) |
| output_tensor_height  |   Y       | integer   | Output tensor size (height) |
| output_tensor_width   |   Y       | integer   | Output tensor size (width) |
| traffic_counting      |   Y       | array of LineString or Polygon     | Boundary coordinates for traffic counting |
| bike_counting         |   Y       | array of LineString or Polygon  | Boundary coordinates for bike counting |
| pedestrian_counting   |   Y       | array of LineString or Polygon    | Boundary coordinates for pedestrian counting |
| parking_zone          |   N       | array of Polygon     | Parking zone coordinates |

#### output
| Field Name | Required  | Data Type | Description |
|------------|-----------|-----------|-------------|
| frame_id  |   Y       | integer    | Unique identifier for the frame |
| timestamp  |   N       | string    | The timestamp of the frame in ISO 8601 format |
| object_ids   |   Y       | array of integer   | List of detected objects in the frame |
| object_bboxes    |   Y       | array     | Bounding box coordinates of the detected object [x1, y1, x2, y2] |
| object_class  |   Y       | array of string    | Type of the detected object (e.g., vehicle, pedestrian) |
| object_scores       |   Y       | array of number    | Confidence score of the detected object |
| traffic_counting       |   Y       | array of integer    | The total number of vehicle that passes the counting boundary |
| bike_counting |   Y       |  array of integer     | The total number of bike that passes the counting boundary |
| pedestrian_counting |   Y       |  array of integer     | The total number of pedestrian that passes the counting boundary |
| parking_status |   N       | boolean     | Parking status (true or false) |