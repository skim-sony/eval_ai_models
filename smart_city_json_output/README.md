# Descriptions for standardized JSON output schema

This README describes the JSON output schema that we standardized for the AITRIOS AI model output. The current JSON output schema (v1.0.0) is primarily intended for DNN object detection and post-processing for smart city use-cases, such as traffic counting and curb management. The website https://www.jsonschemavalidator.net/ is useful for validating output files against the JSON schema during system development.

- [frame_output_schema.json](https://github.com/smart-camera-engagement/eval-ai-models/blob/main/smart_city_json_output/frame_output_schema.json): output schema for frame-based output
- [frame_output_sample.json](https://github.com/smart-camera-engagement/eval-ai-models/blob/main/smart_city_json_output/frame_output_sample.json): output sample

----

### frame_output_schema.json
The 'frame_output_schema.json' file consists of two objects: 'config' and 'output'. Tje 'output' is an array of output object.

#### 'config' object
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
| traffic_counting      |   N       | array of [LineString](https://datatracker.ietf.org/doc/html/rfc7946#appendix-A.2) or [Polygon](https://datatracker.ietf.org/doc/html/rfc7946#appendix-A.3)     | Boundary coordinates for traffic counting |
| bike_counting         |   N       | array of [LineString](https://datatracker.ietf.org/doc/html/rfc7946#appendix-A.2) or [Polygon](https://datatracker.ietf.org/doc/html/rfc7946#appendix-A.3)  | Boundary coordinates for bike counting |
| pedestrian_counting   |   N       | array of [LineString](https://datatracker.ietf.org/doc/html/rfc7946#appendix-A.2) or [Polygon](https://datatracker.ietf.org/doc/html/rfc7946#appendix-A.3)    | Boundary coordinates for pedestrian counting |
| parking_zone          |   N       | array of [Polygon](https://datatracker.ietf.org/doc/html/rfc7946#appendix-A.3)     | Parking zone coordinates |

#### 'output' object
| Field Name | Required  | Data Type | Description |
|------------|-----------|-----------|-------------|
| frame_id  |   Y       | integer    | Unique identifier for the frame |
| timestamp  |   N       | string    | The timestamp of the frame in ISO 8601 format |
| object_id   |   Y       | array of integer   | List of detected objects in the frame |
| object_bbox    |   Y       | array     | Bounding box coordinates of the detected object [x1, y1, x2, y2] |
| object_class  |   Y       | array of string    | Type of the detected object (supported objects: "pedestrian", "bicycle", "cargo_bicycle", "car", "scooter", "moped", "motorcycle", "truck", "van", "freight", "other", "unspecified")|
| object_score       |   Y       | array of number    | Confidence score of the detected object |
| traffic_counting       |   N       | array of integer    | The total number of vehicle that passes the counting boundary |
| bike_counting |   N       |  array of integer     | The total number of bike that passes the counting boundary |
| pedestrian_counting |   N       |  array of integer     | The total number of pedestrian that passes the counting boundary |
| parking_status |   N       | object     | Parking status ([details](https://github.com/smart-camera-engagement/eval-ai-models/tree/main/smart_city_json_output#more-details-on-parking-status)) |

##### Details on 'parking_status' object
| Field Name | Required  | Data Type | Description |
|------------|-----------|-----------|-------------|
| occupied |   Y       | array of boolean     | Parking status for each parking zone in the current frame (true or false) |
| parking_dwell_time |   Y       | array of integer     | Parking dwell time for each parking zone (unit is seconds) |
| double_parking_status |   N       | object    | Double parking status ([details](https://github.com/smart-camera-engagement/eval-ai-models/tree/main/smart_city_json_output#more-details-on-double-parking-status)) |

##### Details on 'double_parking_status' object
| Field Name | Required  | Data Type | Description |
|------------|-----------|-----------|-------------|
| status |   Y       | boolean     | Double parking status in the current frame (true or false) |
| double_parking_dwell_time |   N       | integer     | Double parking dwell time in the current frame (unit is seconds) |
| vehicle_blocked_lane_types |   N       | [LaneType](https://github.com/openmobilityfoundation/curb-data-specification/tree/main/events#lane-type)    | Type of lane blocked by the vehicle performing the event. |
| double_parking_location |   N       | array of [Point](https://datatracker.ietf.org/doc/html/rfc7946#appendix-A.1) or [Polygon](https://datatracker.ietf.org/doc/html/rfc7946#appendix-A.3)    | Double parking location coordinates |


----
### Version
|   Version  |   Date    | Description |
|------------|-----------|-------------|
| 1.0.0      | 11/6/2024 | First version created for DNN object detection output and smart city use-case |