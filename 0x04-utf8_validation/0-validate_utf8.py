def validUTF8(data):
    # Number of bytes remaining in the current UTF-8 character
    remaining_bytes = 0
    
    for num in data:
        # Get the 8 least significant bits of the integer
        byte = num & 0xFF

        if remaining_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            if (byte >> 5) == 0b110:
                remaining_bytes = 1  # 2-byte character
            elif (byte >> 4) == 0b1110:
                remaining_bytes = 2  # 3-byte character
            elif (byte >> 3) == 0b11110:
                remaining_bytes = 3  # 4-byte character
            elif (byte >> 7) != 0:
                return False  # 1-byte character must start with 0
        else:
            # Continuation byte must start with 10
            if (byte >> 6) != 0b10:
                return False
            remaining_bytes -= 1

    # If all bytes are processed, remaining_bytes should be 0 for valid encoding
    return remaining_bytes == 0

