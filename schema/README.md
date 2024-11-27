# Descriptions for standardized JSON output schema

This README describes the JSON output schema that we standardized for the AITRIOS AI model output. The current JSON output schema (v1.0.1) is primarily intended for DNN object detection and post-processing for smart city use-cases, such as traffic counting and curb management. It can be expanded  to more use-cases and can be easily added to the main schema. 

Below is the link to the main schema files:
- [config_main_schema.json](https://github.com/smart-camera-engagement/eval-ai-models/blob/v1.0.1/schemas/config_main_schema.json): config main schema to log configurations and settings of AI model and algorithm.
- [output_main_schema.json](https://github.com/smart-camera-engagement/eval-ai-models/blob/v1.0.1/schemas/output_main_schema.json): output main schema for frame-based or event outputs

----

### config_main_schema.json
The 'config_main_schema.json' file consists of several subschemas: 'general_config', 'counting_config' and 'curb_config'.

#### 'general_config' object
| Field Name            | Required  | Data Type | Description |
|-----------------------|-----------|-----------|-------------|
| source_type           |   Y       | string    | Source type for data |
| camera_id             |   Y       | integer   | Camera id |
| video_file_name       |   N       | string    | Video file name; leave as 'null' if it's online processing |
| total_image_frames    |   N       | integer   | The number of total images for processing; leave as -1 if it's online processing |
| input_tensor_height   |   Y       | integer   | Input tensor size (height) |
| input_tensor_width    |   Y       | integer   | Input tensor size (width) |
| output_tensor_height  |   Y       | integer   | Output tensor size (height) |
| output_tensor_width   |   Y       | integer   | Output tensor size (width) |

#### 'counting_config' object
| Field Name            | Required  | Data Type | Description |
|-----------------------|-----------|-----------|-------------|
| counting_type   |   Y       | string   | Type of count measurement (supported types: "total", "peak", "average") |
| counting_frequency   |   Y       | object   | Frequency of count measurement (unit: "frame", "second", "minute") |
| counting_boundary   |   Y       | array   | Boundary configuration for traffic counting ([LineString](https://datatracker.ietf.org/doc/html/rfc7946#appendix-A.2) and [Polygon](https://datatracker.ietf.org/doc/html/rfc7946#appendix-A.3) are supported for geometry.)|

#### 'curb_config' object
| Field Name            | Required  | Data Type | Description |
|-----------------------|-----------|-----------|-------------|
| zone   |   Y       | array   | Zone configuration for curb management (supported curb_zone_id: "parking_zone_0", "parking_zone_1", "loading_zone_0", "loading_zone_1", "bike_lane_0", "bike_lane_1", "traffic_lane_0", "traffic_lane_1", "sidewalk_0", "sidewalk_1") |
| space   |   Y       | array   | Space configuration for curb management (supported curb_space_id: "parking_space_0", "parking_space_1", "parking_space_2", "parking_space_3", "parking_space_4", "parking_space_5", "parking_space_6", "parking_space_7", "parking_space_8", "parking_space_9") |

### output_main_schema.json
The 'output_main_schema.json' file can be used for both frame-based output and event-based output. Frame-based output is primarily for evaluation purposes, while event-based output is intended for system integration with the dashboard. The main schema consists of several subschemas: 'detection_results', 'counting_results', 'parking_results' and 'curb_management_results'.
| Field Name | Required  | Data Type | Description |
|------------|-----------|-----------|-------------|
| frame_id  |   Y       | integer    | Unique identifier for the frame |
| timestamp  |   N       | string    | The timestamp of the frame in ISO 8601 format |

#### 'detection_results' object
| Field Name | Required  | Data Type | Description |
|------------|-----------|-----------|-------------|
| object_id   |   Y       | array of integer   | List of detected objects in the frame |
| object_bbox    |   Y       | array     | Bounding box coordinates of the detected object [x1, y1, x2, y2] |
| object_class  |   Y       | array of string    | Type of the detected object (supported objects: "pedestrian", "bicycle", "cargo_bicycle", "car", "scooter", "moped", "motorcycle", "truck", "van", "freight", "other", "unspecified")|
| object_score       |   Y       | array of number    | Confidence score of the detected object |


----
### Version
|   Version  |   Date    | Description |
|------------|-----------|-------------|
| 1.0.0      | 11/6/2024 | First version created for DNN object detection output and smart city use-case |
| 1.0.1      | 11/15/2024 | Updated the main schema into separate subschemas depending on use-case |