# Lab 3 & 4 - Synchronizing a Battery Asset Administration Shell (AAS) with Node-RED

## Overview

In the previous lab, you designed a **Battery Asset Administration Shell (AAS)** and created a battery submodel containing several battery properties.

In this lab, you will connect your Battery AAS to an emulated battery data source using **Node-RED**.

The objective is to implement a simple synchronization mechanism that continuously updates AAS properties from emulated measurements.

This architecture is an example of a **Digital Shadow**, a fundamental building block of a Digital Twin.

---

# Learning Objectives

After completing this lab, you should be able to:

- Understand the role of data synchronization in a Digital Twin.
- Create Node-RED workflows.
- Consume data from REST APIs.
- Update AAS properties through REST interfaces.
- Synchronize a virtual asset representation with its physical (or emulated) system.
- Explain the difference between:
  - Digital Model
  - Digital Shadow
  - Digital Twin

---

# System Architecture

```text
+----------------------------+
| Battery Simulation Service |
+-------------+--------------+
              |
              | HTTP GET
              v
+----------------------------+
|         Node-RED           |
|                            |
|  Read battery data         |
|  Process measurements      |
|  Update AAS properties     |
+-------------+--------------+
              |
              | HTTP PUT
              v
+----------------------------+
|        Battery AAS         |
+----------------------------+
```

---

# Scenario

You will synchronize the following battery properties:

- Voltage_measured
- Current_measured
- Temperature_measured
- Time

The simulator generates values periodically.

Node-RED retrieves these values and updates the Battery AAS.

---

# Prerequisites

Before starting, make sure that:

- The AAS Environment is running.
- The Battery AAS created during TP2 is available.
- Node-RED is installed and running (e.g. http://localhost:1880).
- The battery emulation service is available (e.g. http://localhost:5000).
- You can access both systems from your web browser.

---

# Step 1 - Verify Your Battery AAS

Open the AAS Environment and verify that your Battery Submodel contains at least the following properties:

```text
BatterySubModel
├── Voltage_measured
├── Current_measured
├── Temperature_measured
└── Time
```

Keep the Submodel Identifier available.

You will need it later when configuring the REST endpoints.

---

# Step 2 - Test the Battery Simulation Service

The Battery Emulator exposes the following endpoint:

```http
GET http://localhost:5000/battery
```

Example response:

```json
{
  "batteryId": "battery-001",
  "Voltage_measured": 3.72,
  "Current_measured": 1.13,
  "Temperature_measured": 26.4,
  "Time": "2026-01-12T14:25:00Z"
}
```

Verify that the endpoint returns data:

```bash
curl http://localhost:5000/battery
```

---

# Step 3 - Create the Node-RED Flow

## 3.1 Create a Periodic Trigger

Add an **Inject** node.

Configuration:

```text
Repeat every 5 seconds
```

Purpose:

```text
Trigger battery synchronization periodically.
```

---

## 3.2 Read the Battery Data

Add an **HTTP Request** node.

Configuration:

```text
Method: GET
URL: http://battery-emulator:5000/battery
Return: Parsed JSON Object
```

> Since Node-RED runs inside Docker, do not use `localhost`.
>
> Use the Docker service name:
>
> ```text
> http://battery-emulator:5000/battery
> ```

Connect the Inject node to the HTTP Request node.

---

## 3.3 Extract the Measurements

Add a **Function** node after the HTTP Request node.

```javascript
msg.voltage = msg.payload.Voltage_measured;
msg.current = msg.payload.Current_measured;
msg.temperature = msg.payload.Temperature_measured;
msg.time = msg.payload.Time;

return msg;
```

Purpose:

```text
Store battery measurements in reusable variables.
```

---

# Step 4 - Update Battery Properties in the AAS

The BaSyx API endpoint:

```text
.../submodel-elements/<Property>/$value
```

expects a single JSON value, not a JSON object.

For example:

Valid payload

```json
"3.44"
```

Invalid payload

```json
{
  "value": "3.44"
}
```

---

## 4.1 Update Voltage_measured

### Function Node

```javascript
msg.method = "PATCH";

msg.headers = {
    "Content-Type": "application/json"
};

msg.payload = '"' + msg.voltage + '"';

return msg;
```

### HTTP Request Node

Configuration:

```text
Method: set by msg.method
Return: Parsed JSON Object
```

Example URL:

```text
http://aas-env:8081/submodels/<SUBMODEL_ID>/submodel-elements/Voltage_measured/$value
```

---

## 4.2 Update Current_measured

### Function Node

```javascript
msg.method = "PATCH";

msg.headers = {
    "Content-Type": "application/json"
};

msg.payload = '"' + msg.current + '"';

return msg;
```

### HTTP Request Node

Example URL:

```text
http://aas-env:8081/submodels/<SUBMODEL_ID>/submodel-elements/Current_measured/$value
```

---

## 4.3 Update Temperature_measured

### Function Node

```javascript
msg.method = "PATCH";

msg.headers = {
    "Content-Type": "application/json"
};

msg.payload = '"' + msg.temperature + '"';

return msg;
```

### HTTP Request Node

Example URL:

```text
http://aas-env:8081/submodels/<SUBMODEL_ID>/submodel-elements/Temperature_measured/$value
```

---

## 4.4 Update Time

### Function Node

```javascript
msg.method = "PATCH";

msg.headers = {
    "Content-Type": "application/json"
};

msg.payload = '"' + msg.time + '"';

return msg;
```

### HTTP Request Node

Example URL:

```text
http://aas-env:8081/submodels/<SUBMODEL_ID>/submodel-elements/Time/$value
```

---

# Complete Flow

Your final workflow should look similar to:

```text
Inject (every 5 s)
        |
        v
HTTP GET Battery Emulator
        |
        v
Function (Extract Measurements)
        |
        +------> Function → PATCH Voltage_measured
        |
        +------> Function → PATCH Current_measured
        |
        +------> Function → PATCH Temperature_measured
        |
        +------> Function → PATCH Time
```

---

# Step 5 - Verify Synchronization

Deploy your Node-RED flow.

Verify that the Battery Emulator returns live values:

```json
{
  "Voltage_measured": 3.81,
  "Current_measured": 1.47,
  "Temperature_measured": 28.2,
  "Time": "2026-08-14T17:26:44Z"
}
```

Then verify that the same values are visible in the corresponding AAS properties.

The values should be updated automatically every few seconds.

---
