def test_write():
    filename = "/Users/abisheek/Library/Mobile Documents/com~apple~CloudDocs/Desktop/face regonination project/schoolattendance.csv"
    try:
        with open(filename, "a") as f:
            f.write("test_write\n")
        print("Write successful")
    except Exception as e:
        print(f"Write failed: {e}")
test_write()
