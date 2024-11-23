import os
from PIL import Image
import pytesseract
import tiktoken

def extract_text_from_images(folder_path):
    extracted_texts = []
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
            image_path = os.path.join(folder_path, filename)
            try:
                text = pytesseract.image_to_string(Image.open(image_path))
                extracted_texts.append(text)
            except Exception as e:
                print(f"Error processing {filename}: {e}")
    return extracted_texts

def count_tokens(text, model_name='gpt-3.5-turbo'):
    encoding = tiktoken.encoding_for_model(model_name)
    tokens = encoding.encode(text)
    return len(tokens)

def split_large_text(text, min_tokens, max_tokens, encoding):
    tokens = encoding.encode(text)
    splits = []
    start = 0
    while start < len(tokens):
        end = start + max_tokens
        chunk_tokens = tokens[start:end]
        chunk_text = encoding.decode(chunk_tokens)
        splits.append(chunk_text)
        start = end
    return splits

def split_text_into_chunks(texts, min_tokens=3000, max_tokens=7000, model_name='gpt-3.5-turbo'):
    encoding = tiktoken.encoding_for_model(model_name)
    chunks = []
    current_chunk = ''
    current_chunk_tokens = 0

    for text in texts:
        text_tokens = encoding.encode(text)
        text_token_count = len(text_tokens)

        if current_chunk_tokens + text_token_count <= max_tokens:
            current_chunk += text + '\n'
            current_chunk_tokens += text_token_count
        else:
            if current_chunk_tokens >= min_tokens:
                chunks.append(current_chunk)
                current_chunk = text + '\n'
                current_chunk_tokens = text_token_count
            else:
                # Handle cases where a single text exceeds max_tokens
                if text_token_count > max_tokens:
                    split_texts = split_large_text(text, min_tokens, max_tokens, encoding)
                    for split_text in split_texts:
                        chunks.append(split_text)
                    current_chunk = ''
                    current_chunk_tokens = 0
                else:
                    current_chunk += text + '\n'
                    current_chunk_tokens += text_token_count

    if current_chunk_tokens >= min_tokens:
        chunks.append(current_chunk)
    elif chunks:
        chunks[-1] += current_chunk
    else:
        chunks.append(current_chunk)

    return chunks

def save_chunks_to_files(chunks, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for i, chunk in enumerate(chunks):
        file_path = os.path.join(output_folder, f'chunk_{i+1}.txt')
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(chunk)

def main(input_folder, output_folder):
    print("Extracting text from images...")
    texts = extract_text_from_images(input_folder)
    print(f"Extracted text from {len(texts)} images.")

    print("Splitting text into chunks...")
    chunks = split_text_into_chunks(texts)
    print(f"Created {len(chunks)} text chunks.")

    print("Saving chunks to files...")
    save_chunks_to_files(chunks, output_folder)
    print(f"Saved chunks to '{output_folder}'.")

if __name__ == "__main__":
    input_folder = '/c/Users/aerot/coding/extract-text/xander/'  # Replace with your images folder path
    output_folder = '/c/Users/aerot/coding/extract-text/output/'      # Replace with your output folder path
    main(input_folder, output_folder)
