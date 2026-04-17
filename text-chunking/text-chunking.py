def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    """
    # Write code here

    if chunk_size <= 0:
        return None

    if overlap >= chunk_size:
        return None

    chunks = []

    step_size = chunk_size - overlap

    for i in range(0, len(tokens), step_size):
        chunk = tokens[i:i + chunk_size]
        if chunk:
            chunks.append(chunk)

        if i + chunk_size >= len(tokens):
            break
    return chunks