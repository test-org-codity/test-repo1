def clamp(value, minimum, maximum):
    if minimum > maximum:
        raise ValueError("minimum exceeds maximum")
    return max(minimum, min(value, maximum))
