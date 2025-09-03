# Example: Iterative Geocoding with GISDK + Python

This example demonstrates how to **geocode a dataset iteratively** using the **Caliper Maptitude GISDK** via the `caliperpy` Python API.  
The script processes a view or table containing address information and attempts to locate each record in **three passes**, saving unmatched records in **selection sets** for further review.

---

## How the Geocoding Passes Work

### **Pass 1 — Address + ZIP**
- Uses the **ADDRESS** method.
- Attempts to locate each record using the **street address** and **postal code**.
- Creates a **new geocoded layer** and automatically generates a **selection set** for **unmatched records**.

### **Pass 2 — Retry Unmatched Records**
- Processes the **selection set** of unmatched records from Pass 1.
- Runs the **ADDRESS** method again using updated field specifications from the new layer.
- Reduces the number of unlocated records.

### **Pass 3 — City + State**
- For records **still unmatched** after Pass 2:
    - Uses the **CITY** method.
    - Locates records based on **city** and **state** only, ignoring street addresses.
    - Maximizes the overall match rate when only partial data is available.

---

## Inputs

- A Maptitude **view or table** with:
  - Address
  - ZIP (postal code)
  - City
  - State
- **Maptitude 2025 or newer** with GISDK installed and licensed.
- `caliperpy` Python library installed.
- Access to the **Maptitude Tutorial data** (if required by the script).

---

## Outputs

- A **new geocoded layer** saved as a `.dbd` database file in the output folder (default: `C:\temp\`).
- The new layer contains a selection set  **(NotFoundSet)** containing the records that could **not** be geocoded.

---

## How to Run
1. Open Maptitude manually
2. Open the ParcelInfo.bin table, located in the Tutorial folder:
    "C:\Users\[USERNAME]\Documents\Caliper\Maptitude YYYY\Tutorial\ParcelInfo.bin"

```bash
python Geocoding.py
