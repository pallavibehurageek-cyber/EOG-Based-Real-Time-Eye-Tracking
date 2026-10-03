import serial
import pandas as pd
import csv
import time
 
output_excel_file_path = "checkVer.csv"

# Set a timeout to avoid blocking indefinitely
ser1 = serial.Serial(port='COM17', baudrate=2000000, timeout=1)
ser2 = serial.Serial(port='COM3',baudrate=2000000,timeout=1)

# def labelling(timestamp):
#     if(timestamp % 2 > 0.3 and timestamp % 2 < 0.9):
#         if((timestamp // 2) % 4 == 1):
#             return 0
#         elif((timestamp // 2) % 4 == 2):
#             return 0
#         else:
#             return 2
#     else:
#         return 1 # 6-8 C  8-10 R 10 - 12 C  12 - 14 L

with open(output_excel_file_path, 'w', newline='') as file:
    time.sleep(1)
    writer = csv.writer(file)
    writer.writerow(['Timestamp', 'Data1','Data2'])
    try: 
        while True:
            line1 = ser1.readline()
            # print("Waiting for data...")
            line2 =ser2.readline()
            if (not line1) or (not line2):
                print("No data received. Retrying...")
                continue
            line1 = line1.decode('utf-8').strip()
            line1 = line1.split(",")
            line2 = line2.decode('utf-8').strip()
            line2 = line2.split(",")
            # print("Processed line: ", line)
            if len(line1) != 2:
                print("Incomplete data received: ", line1)
                continue
            if len(line2) !=2:
                print("Incomplete data received: ", line1)
                continue
            timestamp = (float(line1[0])+float(line2[0]))/2
            # print(timestamp)
            # line.append(labelling(timestamp))
            if timestamp >= 6:
                line=[timestamp,line1[1],line2[1]]
                # print(line)
                writer.writerow(line)
                # file.flush()
    except KeyboardInterrupt:
        print("Done")
    except serial.SerialException as se:
        print("SerialException:", se)
    except Exception as e:
        print("Error:", e)
    finally:
        file.close()
        ser1.close()
        ser2.close()
