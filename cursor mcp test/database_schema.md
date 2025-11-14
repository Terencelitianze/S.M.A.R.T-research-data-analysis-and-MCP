# Database Schema Documentation

## Overview

This document provides a comprehensive description of the database schema for the sensors monitoring system. The database is built on MySQL and uses Django's ORM for management.

## Table Structure

### Core Sensor Tables

#### sensor_data_component

Stores physical information about sensor components.

- `id` (bigint, PRIMARY KEY): Unique identifier
- `name` (varchar): Component name
- `floor` (int): Floor location
- `length_mm` (int): Length in millimeters
- `height_mm` (int): Height in millimeters
- `width_mm` (int): Width in millimeters
- `weight_t` (double): Weight in tons
- `production_time` (date): Production date
- `installation_time` (date): Installation date

#### sensor_data_state

Records sensor state readings.

- `state_id` (int, PRIMARY KEY): Unique state identifier
- `state` (double): Sensor state value
- `last_updated_ts` (datetime): Timestamp of last update
- `metadata_id_id` (int, FOREIGN KEY): Reference to sensor_data_statemeta

#### sensor_data_statemeta

Contains metadata about sensor states.

- `metadata_id` (int, PRIMARY KEY): Unique metadata identifier
- `entity_id` (varchar): Entity identifier

#### sensor_ids

Stores sensor identification information.

- `id` (int, PRIMARY KEY): Unique sensor identifier
- `name` (varchar): Sensor name

### Environmental Quality Monitoring

#### indoor_environmental_quality_index

Tracks comprehensive indoor environmental quality metrics.

- `id` (int, PRIMARY KEY): Unique record identifier
- `update_time_id` (int, FOREIGN KEY): Reference to update time
- `sensor_name_id` (int, FOREIGN KEY): Reference to sensor
- `friendly_sensor_name` (varchar): Human-readable sensor name
- `friendly_update_time` (timestamp): Human-readable update time
- `index_value` (float): Overall quality index
- `thermal` (float): Thermal comfort metric
- `light` (float): Lighting quality metric
- `air` (float): Air quality metric
- `acoustic` (float): Acoustic quality metric
- `air_pm25` (float): PM2.5 air quality metric
- `air_voc` (float): VOC air quality metric
- `ppd_thermal` (float): Percentage of People Dissatisfied (thermal)
- `ppd_light` (float): Percentage of People Dissatisfied (lighting)
- `ppd_air` (float): Percentage of People Dissatisfied (air)
- `ppd_acoustic` (float): Percentage of People Dissatisfied (acoustic)
- `ppd_pm25` (float): Percentage of People Dissatisfied (PM2.5)
- `ppd_voc` (float): Percentage of People Dissatisfied (VOC)
- `contri_thermal` (float): Thermal contribution factor
- `contri_light` (float): Lighting contribution factor
- `contri_air` (float): Air quality contribution factor
- `contri_acoustic` (float): Acoustic contribution factor

#### indoor_environmental_quality_index_daily

Daily aggregated environmental quality metrics.

- `id` (int, PRIMARY KEY): Unique record identifier
- `sensor_name_id` (int, FOREIGN KEY): Reference to sensor
- `update_time_id` (int, FOREIGN KEY): Reference to update time
- `friendly_sensor_name` (varchar): Human-readable sensor name
- `friendly_update_date` (date): Human-readable update date
- `index_value` (float): Overall quality index
- `thermal` (float): Thermal comfort metric
- `light` (float): Lighting quality metric
- `air` (float): Air quality metric
- `acoustic` (float): Acoustic quality metric

### Occupancy Tracking

#### occupancy_records

Records individual occupancy data points.

- `record_id` (int, PRIMARY KEY): Unique record identifier
- `grid_x` (int): X-coordinate in grid
- `grid_y` (int): Y-coordinate in grid
- `timestamp` (datetime): Record timestamp
- `total_duration_seconds` (float): Total duration in seconds
- `avg_people` (float): Average number of people
- `peak_people` (int): Peak number of people

#### total_occupancy_records

Aggregated occupancy statistics.

- `record_id` (int, PRIMARY KEY): Unique record identifier
- `timestamp` (datetime): Record timestamp
- `total_people` (int): Total number of people
- `unique_grids` (int): Number of unique occupied grids
- `avg_people` (float): Average number of people
- `peak_people` (int): Peak number of people
- `total_duration_seconds` (float): Total duration in seconds
- `area_coverage_percentage` (float): Percentage of area covered

### Statistics and Analysis

#### sensor_statistics_hourly

Hourly aggregated sensor statistics.

- `id` (int, PRIMARY KEY): Unique record identifier
- `update_time_id` (int, FOREIGN KEY): Reference to update time
- `metadata_id` (int, FOREIGN KEY): Reference to metadata
- `average` (float): Average value
- `deviation` (float): Standard deviation
- `median` (float): Median value
- `max_state` (float): Maximum value
- `min_state` (float): Minimum value
- `q1_state` (float): First quartile
- `q3_state` (float): Third quartile
- `weighted_averge` (float): Weighted average

#### sensor_statistics_coorelation

Correlation analysis data.

- `update_time_id` (int, PRIMARY KEY): Unique record identifier
- `timestamp` (double): Timestamp

### Forecasting

#### forecast_pm25

PM2.5 forecast data.

- `id` (int, PRIMARY KEY): Unique record identifier
- `timestamp` (datetime): Forecast timestamp
- `forecasted_data` (float): Forecasted PM2.5 value
- `sensor_id` (int, FOREIGN KEY): Reference to sensor

### Django Framework Tables

#### auth_user

User authentication information.

- `id` (int, PRIMARY KEY): User identifier
- `password` (varchar): Hashed password
- `last_login` (datetime): Last login timestamp
- `is_superuser` (tinyint): Superuser flag
- `username` (varchar): Username
- `first_name` (varchar): First name
- `last_name` (varchar): Last name
- `email` (varchar): Email address
- `is_staff` (tinyint): Staff flag
- `is_active` (tinyint): Active flag
- `date_joined` (datetime): Account creation date

#### auth_group

User groups.

- `id` (int, PRIMARY KEY): Group identifier
- `name` (varchar): Group name

#### auth_permission

User permissions.

- `id` (int, PRIMARY KEY): Permission identifier
- `name` (varchar): Permission name
- `content_type_id` (int, FOREIGN KEY): Content type reference
- `codename` (varchar): Permission code

#### django_session

User sessions.

- `session_key` (varchar, PRIMARY KEY): Session identifier
- `session_data` (longtext): Session data
- `expire_date` (datetime): Session expiration date

## Relationships

1. `sensor_data_state` -> `sensor_data_statemeta` (metadata_id_id -> metadata_id)
2. `forecast_pm25` -> `sensor_ids` (sensor_id -> id)
3. `indoor_environmental_quality_index` -> `sensor_ids` (sensor_name_id -> id)
4. `sensor_statistics_hourly` -> `sensor_data_statemeta` (metadata_id -> metadata_id)
5. `states` -> `states_meta` (metadata_id -> metadata_id)

## Notes

- All timestamps are stored in UTC
- Foreign key relationships are maintained through Django's ORM
- The database uses InnoDB as the storage engine
- All tables use auto-incrementing primary keys
- Most numeric values are stored as float or double for precision
- String fields use varchar with appropriate lengths
- Boolean values are stored as tinyint(1)
