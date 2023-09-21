import requests
import pickle
import numpy as np

def download_file(url, filename):
    # Download the file from the given URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Save the content into a file
        with open(filename, 'wb') as f:
            f.write(response.content)
    else:
        print("Failed to download the file.")

def load_and_unpickle(filename):
    # Load and unpickle the object from a file
    with open(filename, 'rb') as f:
        unpickled_object = pickle.load(f)
    return unpickled_object

def main():
    url = 'https://dataverse.harvard.edu/api/access/datafile/6934320'
    filename = 'downloaded_file.pkl'
    
    # Step 1: Download the file
    download_file(url, filename)
    
    # Step 2: Load and unpickle the object
    try:
        unpickled_object = load_and_unpickle(filename)
    except Exception as e:
        print(f"An error occurred while unpickling the object: {e}")
        return
    
    # Step 3: Analyze the unpickled object
    print("Type of the unpickled object:", type(unpickled_object))
    
    if isinstance(unpickled_object, dict):
        print("It's a dictionary!")
        print("Keys:", unpickled_object.keys())
    elif isinstance(unpickled_object, list):
        print("It's a list!")
        print("Length:", len(unpickled_object))
    elif isinstance(unpickled_object, set):
        print("It's a set!")
        print("Length:", len(unpickled_object))
    elif isinstance(unpickled_object, np.ndarray):
        print("It's a NumPy array!")
        print("Shape:", unpickled_object.shape)
        timer = 0
        for i in unpickled_object:
            timer += 1
            if timer < 20:
                print(i)
            else:
                break
        print("Dimensions:", unpickled_object.ndim)
        print("Data Type:", unpickled_object.dtype)
        print("Size:", unpickled_object.size)
        print("Min Value:", np.min(unpickled_object))
        print("Max Value:", np.max(unpickled_object))
        print("Mean:", np.mean(unpickled_object))
        print("Standard Deviation:", np.std(unpickled_object))
    else:
        print("It's something else.")
        print("Content:", unpickled_object)

if __name__ == '__main__':
    main()
