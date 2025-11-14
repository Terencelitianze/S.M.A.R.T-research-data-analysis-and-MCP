# Database Structure Documentation

## Overview

This document describes the structure of the sensors_database, which appears to be a Django-based database for an environmental monitoring system. The database tracks sensor data, environmental quality metrics, occupancy, and includes forecasting capabilities.

## Table Structure

### Core Sensor Tables

#### sensor_data_component

- **Purpose**: Stores physical sensor information
- **Fields**:
  - `id` (bigint, PRIMARY KEY, auto_increment)
  - `name` (varchar(255))
  - `floor` (int)
  - `length_mm` (int)
  - `height_mm` (int)
  - `width_mm` (int)
  - `weight_t` (double)
  - `production_time` (date)
  - `installation_time` (date)

#### sensor_data_state

- **Purpose**: Records sensor readings and states
- **Fields**:
  - `state_id` (int, PRIMARY KEY, auto_increment)
  - `state` (double)
  - `last_updated_ts` (datetime(6))
  - `metadata_id_id` (int, FOREIGN KEY)

### Environmental Quality Monitoring

#### indoor_environmental_quality_index

- **Purpose**: Stores comprehensive indoor environmental quality metrics
- **Fields**:
  - `id` (int, PRIMARY KEY, auto_increment)
  - `update_time_id` (int, FOREIGN KEY)
  - `sensor_name_id` (int, FOREIGN KEY)
  - `friendly_sensor_name` (varchar(255))
  - `friendly_update_time` (timestamp)
  - `index_value` (float)
  - `thermal` (float)
  - `light` (float)
  - `air` (float)
  - `acoustic` (float)
  - `air_pm25` (float)
  - `air_voc` (float)
  - `ppd_thermal` (float)
  - `ppd_light` (float)
  - `ppd_air` (float)
  - `ppd_acoustic` (float)
  - `ppd_pm25` (float)
  - `ppd_voc` (float)
  - `contri_thermal` (float)
  - `contri_light` (float)
  - `contri_air` (float)
  - `contri_acoustic` (float)

### Occupancy Tracking

#### occupancy_records

- **Purpose**: Tracks occupancy data
- **Note**: Table structure not fully examined, but likely contains occupancy metrics

#### total_occupancy_records

- **Purpose**: Stores aggregated occupancy statistics
- **Note**: Table structure not fully examined, but likely contains summary statistics

### Forecasting

#### forecast_pm25

- **Purpose**: Contains PM2.5 forecast data
- **Note**: Table structure not fully examined, but likely contains forecast values and timestamps

### Statistics and Analysis

#### sensor_statistics_hourly

- **Purpose**: Aggregates sensor data on an hourly basis
- **Note**: Table structure not fully examined, but likely contains hourly aggregated metrics

#### sensor_statistics_coorelation

- **Purpose**: Stores correlation data between different sensors
- **Note**: Table structure not fully examined, but likely contains correlation coefficients

### State Management

#### states

- **Purpose**: Tracks system states
- **Note**: Table structure not fully examined, but likely contains state definitions

#### states_meta

- **Purpose**: Contains metadata about system states
- **Note**: Table structure not fully examined, but likely contains state metadata

### Django Framework Tables

These are standard Django tables for authentication and content management:

- `auth_group`
- `auth_group_permissions`
- `auth_permission`
- `auth_user`
- `auth_user_groups`
- `auth_user_user_permissions`
- `django_admin_log`
- `django_content_type`
- `django_migrations`
- `django_session`

## Key Relationships

1. `sensor_data_state` references `sensor_data_statemeta` through `metadata_id_id`
2. `indoor_environmental_quality_index` references:
   - `update_time_id` (likely to a time-related table)
   - `sensor_name_id` (likely to `sensor_ids` or similar)

## Data Types and Conventions

- Primary keys are typically auto-incrementing integers
- Timestamps are stored as datetime(6) or timestamp
- Measurements are stored as float or double
- Text fields use varchar(255)
- Foreign keys are typically integers

## System Purpose

The database appears to be designed for a comprehensive environmental monitoring system that:

1. Tracks physical sensor characteristics and installation details
2. Records real-time sensor readings and states
3. Monitors indoor environmental quality across multiple factors
4. Tracks occupancy patterns
5. Provides air quality forecasting
6. Generates statistical analysis and correlations
7. Manages system states and metadata
8. Handles user authentication and access control through Django

## Notes for LLM Processing

- All table names are lowercase with underscores
- Foreign key relationships are indicated by `_id` suffix
- Timestamps are stored in high precision (6 decimal places)
- The database follows Django's naming conventions
- Environmental metrics are stored as floating-point numbers
- The system appears to be focused on indoor environmental quality monitoring
