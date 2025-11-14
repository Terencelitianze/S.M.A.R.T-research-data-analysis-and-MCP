# S.M.A.R.T Research Lab Database Documentation

## Database Configuration

- **Host**: 10.224.16.61
- **Port**: 53306
- **Database**: sensors_database
- **User**: smart_intern
- **Access Level**: Read-only (INSERT, UPDATE, DELETE operations are disabled)

## Database Schema Overview

### Core Tables

#### sensor_data_component

Primary table for sensor component information:

- `id` (bigint, PRIMARY KEY): Unique identifier
- `name` (varchar(255)): Component name
- `floor` (int): Floor location
- `length_mm` (int): Length in millimeters
- `height_mm` (int): Height in millimeters
- `width_mm` (int): Width in millimeters
- `weight_t` (double): Weight in tons
- `production_time` (date): Production date
- `installation_time` (date): Installation date

#### sensor_data_state

Contains sensor state data:

- (Structure to be documented)

#### sensor_ids

Contains sensor identification information:

- (Structure to be documented)

#### sensor_statistics_hourly

Hourly statistics for sensor data:

- (Structure to be documented)

#### sensor_statistics_coorelation

Correlation data between sensors:

- (Structure to be documented)

### Environmental Monitoring Tables

#### forecast_pm25

PM2.5 forecast data:

- (Structure to be documented)

#### indoor_environmental_quality_index

Environmental quality measurements:

- (Structure to be documented)

#### indoor_environmental_quality_index_daily

Daily environmental quality indices:

- (Structure to be documented)

### Occupancy Tracking

#### occupancy_records

Individual occupancy records:

- (Structure to be documented)

#### total_occupancy_records

Aggregated occupancy data:

- (Structure to be documented)

### State Management

#### states

State information:

- (Structure to be documented)

#### states_meta

Metadata for states:

- (Structure to be documented)

### Django Framework Tables

The database includes standard Django framework tables for authentication and content management:

- auth_group
- auth_group_permissions
- auth_permission
- auth_user
- auth_user_groups
- auth_user_user_permissions
- django_admin_log
- django_content_type
- django_migrations
- django_session

## Usage Guidelines

1. All queries are read-only
2. Complex joins may be required for comprehensive data analysis
3. Time-series data is available in hourly and daily aggregations
4. Environmental and occupancy data can be correlated using appropriate join conditions

## Data Relationships

- Sensor components are linked to their states through sensor_ids
- Environmental quality indices are calculated from sensor data
- Occupancy records are tracked both individually and in aggregate
- State information is managed through the states and states_meta tables

## Best Practices

1. Use appropriate indexes when querying large datasets
2. Consider time-based partitioning for time-series data
3. Join sensor data with environmental indices for comprehensive analysis
4. Use the correlation tables for understanding sensor relationships
