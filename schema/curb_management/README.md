# Descriptions for JSON output schema of curb management use-case

This README describes the JSON output schema for curb management, which follows the [Curb Data Specification (CDS)](https://github.com/openmobilityfoundation/curb-data-specification/tree/main). The schema version 1.0.3 is primarily intended for system integration with the Umojo CDS server for the City of San Jose. Most fields are the same as those in the CDS, but some details differ. Below are the modifications from the CDS. 
- event_id: requires an integer rather than a UUID (128-bit unique ID) as used by the CDS.
- event_type: "pass_counting_boundary" is added for traffic/bicycle/pedestrian counting.
- vehicle type: "pedestrian" is added.
- object_id: replaced "vehicle_id" with "object_id". 
- curb_zone_id, curb_area_id, curb_space_id, and curb_object_id are defined as follows :
![curbs](curbs_definition.png)
 - curb_area_id: "s_4th_st"
 - curb_zone_id: "parking_zone_0", "parking_zone_1", "loading_zone_0", "loading_zone_1", "bike_lane_0", "bike_lane_1", "traffic_lane_0", "traffic_lane_1", "sidewalk_0", "sidewalk_1"
 - curb_space_id: "parking_space_0", "parking_space_1", "parking_space_2", "parking_space_3", "parking_space_4", "parking_space_5", "parking_space_6", "parking_space_7", "parking_space_8", "parking_space_9"
 - curb_object_id: "asset_0" (please follow [link](https://github.com/openmobilityfoundation/curb-data-specification/tree/dev/curbs#curb-object) for curb object)

Below is the link to the related files:
- [curb_event_output_schema.json](https://github.com/smart-camera-engagement/eval-ai-models/blob/v1.0.3/schema/curb_management/curb_event_output_schema.json): output schema for event-based curb management output
- [asset_event_output_schema.json](https://github.com/smart-camera-engagement/eval-ai-models/blob/v1.0.3/schema/asset_monitoring/asset_event_output_schema.json): output schema for event-based asset monitoring output
- [event_output_sample.json](https://github.com/smart-camera-engagement/eval-ai-models/blob/v1.0.3/sample/event_output_sample.json): output sample
----

### curb_event_output_schema.json
The 'curb_event_output_schema.json' file consists of an array of curb event objects called 'events'.

#### 'events' object
| Field Name            | Required  | Data Type | Description |
|-----------------------|-----------|-----------|-------------|
| event_id           |   Y       | integer    | Unique identifier of the event that occurred. |
| event_type         |   Y       | string ([EventType](https://github.com/openmobilityfoundation/curb-data-specification/tree/main/events#event-type))   | The event_type that happened for this event. ("pass_counting_boundary" is added for traffic counting event.) |
| event_purpose      |   Y       | string ([EventPurpose](https://github.com/openmobilityfoundation/curb-data-specification/tree/main/events#event-purpose))   | General curb usage purpose that the vehicle performed during the event. Required for sources capable of determining activity type for relevant event_types. |
| event_location     |   Y       | object   | The geographic point location where the event occurred. ([details](https://github.com/smart-camera-engagement/eval-ai-models/tree/main/smart_city_json_output/curb_management#details-on-event_location-object)) |
| event_time         |   Y       | string ([Timestamp](https://github.com/openmobilityfoundation/curb-data-specification/blob/main/general-information.md#timestamp))  | Time at which the event occurred. |
| event_publication_time    |   Y       | string ([Timestamp](https://github.com/openmobilityfoundation/curb-data-specification/blob/main/general-information.md#timestamp))  | Time at which the event became available for consumption by this API. |
| curb_zone_id  |   Y       | string   | ID of the Curb Zone where the event occurred.  |
| curb_area_ids   |   Y       | array of string   | IDs of the Curb Area where the event occurred. Since Curb Areas can overlap, an event may happen in more than one. |
| curb_space_id      |   Y       | string     | ID of the Curb Space where the event occurred. |
| object_id         |   Y       | integer  | Id of the vehicle that occurs the event. |
| vehicle_length   |   N       | integer    | Approximate length of the vehicle that performed the event, in centimeters. Required for sources capable of determining vehicle length.  |
| vehicle_type   |   Y       | string ([VehicleType](https://github.com/openmobilityfoundation/curb-data-specification/tree/main/events#vehicle-type))   | Type of the vehicle that performed the event. |
| vehicle_blocked_lane_types          |   N       | array of [LaneType](https://github.com/openmobilityfoundation/curb-data-specification/tree/main/events#lane-type)    | Type(s) of lane blocked by the vehicle performing the event. If no lanes are blocked by the vehicle performing the event, the array should be empty. |

##### Details on 'event_location' object
The 'event_location' follows GeoJSON standard. 
| Field Name | Required  | Data Type | Description |
|------------|-----------|-----------|-------------|
| type      |   Y       | string     | Whenever a vehicle or device location coordinate measurement is presented, it must be represented as a GeoJSON "Feature" object with a corresponding "properties" object. |
| timestamp |   Y       | string     | Date/time that event occurred. Based on GPS or GNSS clock |
| speed     |   Y       | string     | Estimated speed in meters / sec as reported by the GPS chipset |
| geometry  |   Y       | string     | a GeoJSON geometry of type "Point" as defined in [RFC 7946 3.1.6](https://www.ietf.org/rfc/rfc7946.txt).|

----
### Version
|   Version  |   Date    | Description |
|------------|-----------|-------------|
| 1.0.0      | 11/6/2024 | First version created for SJ curb management |
| 1.0.1      | 11/15/2024 | Updated the main schema into separate subschemas depending on use-case |
| 1.0.2      | 12/20/2024 | Updated traffic counting schema and added asset monitoring schema |
| 1.0.3      | 01/28/2025 | Modified the schema not to use nested objects as UrbanLogiq's ingestion engine is not able to handle them, and added a new schema for pedestrian safety use-case |