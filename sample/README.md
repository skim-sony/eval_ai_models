# JSON sample files

This README describes the JSON sample files that we standardized for the AITRIOS AI model output. There are three sample files: config_sample.json, event_output_sample.json, and frame_output_sample.json.

Below is the link to the files:
- [config_sample.json](https://github.com/smart-camera-engagement/eval-ai-models/blob/v1.0.1/sample/config_sample.json): JSON example for configurations of AI model and algorithm.
- [event_output_sample.json](https://github.com/smart-camera-engagement/eval-ai-models/blob/v1.0.1/sample/event_output_sample.json): JSON example for event-based output that will be used for the system integration of curb management solutions, including traffic counting. For example, if a vehicle passes a counting boundary, this should be recorded here as a new event. 
- [frame_output_sample.json](https://github.com/smart-camera-engagement/eval-ai-models/blob/v1.0.1/sample/frame_output_sample.json): JSON example for frame-based output (mainly for algorithm evaluation). The traffic counting results in this file represent the total count accumulated from frame 0 to frame N.

## Event-based output example for traffic counting 

Here is an example of how to add an event for traffic counting in the `event_output_sample.json` file:

```json
{
    "frame_id": 60,
    "timestamp": "2023-10-01T12:00:00Z",
    "event_id": 2,
    "event_type": "pass_counting_boundary", // [important]
    "event_purpose": "unspecified",
    "event_location": {
      "type": "Feature",
      "properties": { 
        "timestamp": 1696161600000,
        "speed": 1.21
      },
      "geometry": {
        "type": "Point",
        "coordinates": [ -85.7629808, 38.257341 ]
      }
    },
    "event_time": "1696161600000",
    "event_publication_time": "1696161600000",
    "curb_zone_id": "traffic_lane_0",  // [important]
    "curb_area_ids": ["s_4th_st"],
    "object_id": 0,
    "vehicle_length": 670,
    "vehicle_type": "car"  // [important]
  },
  {
    "frame_id": 65,
    "timestamp": "2023-10-01T12:00:00Z",
    "event_id": 3,
    "event_type": "pass_counting_boundary",  // [important]
    "event_purpose": "unspecified",
    "event_location": {
      "type": "Feature",
      "properties": { 
        "timestamp": 1696161600000,
        "speed": 1.21
      },
      "geometry": {
        "type": "Point",
        "coordinates": [ -85.7629808, 38.257341 ]
      }
    },
    "event_time": "1696161600000",
    "event_publication_time": "1696161600000",
    "curb_zone_id": "sidewalk_0",  // [important]
    "curb_area_ids": ["s_4th_st"],
    "object_id": 0,
    "vehicle_length": 670,
    "vehicle_type": "pedestrian"  // [important]
  }
```
----
### Version
|   Version  |   Date    | Description |
|------------|-----------|-------------|
| 1.0.0      | 11/6/2024 | First version created for DNN object detection output and smart city use-case |
| 1.0.1      | 11/15/2024 | Updated the main schema into separate subschemas depending on use-case |