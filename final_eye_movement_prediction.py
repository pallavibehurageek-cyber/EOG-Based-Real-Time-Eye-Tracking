import serial
import joblib
import numpy as np
import psutil

# Set process priority to high and assign to CPU core 0
p = psutil.Process()
p.nice(psutil.HIGH_PRIORITY_CLASS)
p.cpu_affinity([0])

# Load pre-trained models
RCL_model = joblib.load("model/RCL.joblib")
UCD_model = joblib.load("model/UCD.joblib")
B_model = joblib.load("model/blink.joblib")

# Define the window size for data processing and the shift amount
window_size = 50
shift = 2

# Initialize data buffer and state variables
data_buffer = []
rcl_pos = 1
ucd_pos = 1
b_time = -1

# Open serial ports for data reading
ser1 = serial.Serial(port='COM17', baudrate=2000000, timeout=1)
ser2 = serial.Serial(port='COM3', baudrate=2000000, timeout=1)

# Function to clean and convert the line of data to floats
def clean_and_convert(line):
    try:
        return [float(x) for x in line]
    except ValueError:
        return None

try:
    last_valid_line = None
    while True:
        # Read lines from both serial ports
        line1 = ser1.readline()
        line2 = ser2.readline()

        if not line1 or not line2:
            print("No data received. Retrying...")
            continue
        
        # Decode and split the data lines
        line1 = line1.decode('utf-8').strip().split(",")
        line2 = line2.decode('utf-8').strip().split(",")
        timestamp = (float(line1[0]) + float(line2[0])) / 2
        line = [timestamp, line1[1], line2[1]]

        if len(line) != 3 or not all(line):
            print("Incomplete or invalid data received:", line)
            if last_valid_line:
                cleaned_line = last_valid_line
            else:
                continue
        else:
            cleaned_line = clean_and_convert(line)
            if cleaned_line is None:
                print("Invalid data received, using last valid line:", line)
                if last_valid_line:
                    cleaned_line = last_valid_line
                else:
                    continue
            else:
                last_valid_line = cleaned_line

        # Append the cleaned data line to the buffer
        data_buffer.append(cleaned_line)
        
        # Process the data buffer when it contains enough data for a full window
        if len(data_buffer) >= window_size:
            window_data = np.array(data_buffer[:window_size])
            row1 = window_data[:, 1:].astype(float).reshape(1, -1)

            # Predict using the models
            RCL = RCL_model.predict(row1)[0]
            UCD = UCD_model.predict(row1)[0]
            B = B_model.predict(row1)[0]

            if timestamp > 6:
                # Check and send consistent RCL predictions
                if RCL != 1:
                    if rcl_pos != 2 and RCL == 2:
                        rcl_pos += 1
                    if rcl_pos != 0 and RCL == 0:
                        rcl_pos -= 1

                    if rcl_pos == 0:
                        position = "Left"  
                    elif rcl_pos == 1:
                        position = "Horizontal centre"  
                    elif rcl_pos == 2:
                        position = "Right"  
                    print(position)

                if B == 1:
                    print("Blink")

                # Check and send consistent UCD predictions
                if UCD != 1:
                    if ucd_pos != 2 and UCD == 2:
                        ucd_pos += 1
                    if ucd_pos != 0 and UCD == 0:
                        ucd_pos -= 1

                    if ucd_pos == 0:
                        position = "Down"
                    elif ucd_pos == 1:
                        position = "Vertical centre"  # Vertical hold
                    elif ucd_pos == 2:
                        position = "Up"  # Up

                    print(position)

            # Shift the buffer to remove the processed data
            data_buffer = data_buffer[shift:]

except Exception as e:
    print("An error occurred:", str(e))

finally:
    # Close the serial ports
    ser1.close()
    ser2.close()
    print("Done")
