import os
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor

input_folder = "./output"
output_folder = "./pico"

concurrency = 20

def process_single_file(filename):
    if not filename.endswith(".svg"): return
    
    input_path = os.path.join(input_folder, filename)
    output_path = os.path.join(output_folder, filename)
    
    try:
        with open(output_path, "w") as out_file:
            subprocess.run(["picosvg", input_path], stdout=out_file, check=True)
        print(f"Successfully processed: {filename}")
    except Exception as e:
        print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        
    start_time = time.time()
    files = os.listdir(input_folder)

    # 使用 ThreadPoolExecutor 並行處理
    with ThreadPoolExecutor(max_workers=concurrency) as executor:
        executor.map(process_single_file, files)

    end_time = time.time()
    print(f"Conversion complete! Time taken: {end_time - start_time:.2f} seconds")