# JSON sample files

This README describes the JSON sample files that we standardized for the AITRIOS AI model output. There are three sample files: config_sample.json, event_output_sample.json, and frame_output_sample.json.

Below is the link to the files:
- [config_sample.json](https://github.com/smart-camera-engagement/eval-ai-models/blob/v1.0.3/sample/config_sample.json): JSON example for configurations of AI model and algorithm.
- [event_output_sample.json](https://github.com/smart-camera-engagement/eval-ai-models/blob/v1.0.3/sample/event_output_sample.json): JSON example for event-based output that will be used for the system integration of curb management solutions, including traffic counting. For example, if a vehicle passes a counting boundary, this should be recorded here as a new event. 
- [frame_output_sample.json](https://github.com/smart-camera-engagement/eval-ai-models/blob/v1.0.3/sample/frame_output_sample.json): JSON example for frame-based output (mainly for algorithm evaluation). The traffic counting results in this file represent the total count accumulated from frame 0 to frame N.

----
### Version
|   Version  |   Date    | Description |
|------------|-----------|-------------|
| 1.0.0      | 11/6/2024 | First version created for DNN object detection output and smart city use-case |
| 1.0.1      | 11/15/2024 | Updated the main schema into separate subschemas depending on use-case |
| 1.0.2      | 12/20/2024 | Updated traffic counting schema and added asset monitoring schema |
| 1.0.3      | 01/28/2025 | Modified the schema not to use nested objects as UrbanLogiq's ingestion engine is not able to handle them, and added a new schema for pedestrian safety use-case |